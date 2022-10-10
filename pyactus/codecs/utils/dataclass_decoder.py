import dataclasses
import datetime
import enum

from pyactus.codecs.utils import value_convertor as convertor
from pyactus.types.core import Cycle
from pyactus.types.core import Period
from pyactus.types.enums import ENUM_SET
from pyactus.utils import logger
from pyactus.utils.convertors import to_iso_time_interval
from pyactus.utils.convertors import to_pascal_case


def decode_entity(encoded: dict, entity_kls: type):
    """Decodes a domain entity from it's dictionary representation.

    :param encoded: Dictionary representation of a domain entity.
    :param entity_kls: Type of domain entity to be decoded.
    :returns: A decoded domain entity.

    """
    entity: object = entity_kls()
    for fld in dataclasses.fields(entity_kls):
        setattr(entity, fld.name, _get_attr_value(entity, fld, encoded))

    return entity


def _get_attr_value(entity: object, fld: dataclasses.Field, encoded: dict):
    """Returns value of a field declared within a domain entity.

    """
    attr_name: str = to_pascal_case(fld.name)
    for encoded_name in encoded.keys():
        if encoded_name != attr_name:
            continue

        try:
            fld_mapper = _VALUE_MAPPERS[fld.type]
        except KeyError:
            logger.log_warning(f"Unsupported mapping target type: [{fld.type}].")
            break

        try:
            return fld_mapper(encoded[encoded_name], fld.type)
        except NotImplementedError:
            logger.log_warning(f"Unsupported mapping: '{type(entity).__name__}.{fld.name}'")
            break


# Map: Type <-> Mapping function.
_VALUE_MAPPERS = {
    Cycle: convertor.to_cycle,
    Period: convertor.to_period,
    datetime.datetime: lambda val, _: convertor.to_datetime(val),
    datetime.timedelta: lambda val, _: convertor.to_timedelta(val),
    float: lambda val, _: convertor.to_float(val),
    str: lambda val, _: convertor.to_str(val),
} | {i: convertor.to_enum for i in ENUM_SET}
