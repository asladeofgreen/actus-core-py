import dataclasses
import datetime
import enum

from pyactus.codecs.utils import value_convertor as convertor
from pyactus.types.core import Cycle
from pyactus.types.core import Period
from pyactus.types.enums import ENUM_SET
from pyactus.utils import logger
from pyactus.utils.convertors import to_pascal_case


# Set of datetime formats aginst which to parse an externally defined date.
_DATETIME_FORMATS = {
    "%Y",
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S"
}


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
    attr_name = to_pascal_case(fld.name)
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
            logger.log_warning(f"Field {fld.name} of type {fld.type} is unmappeable")
            break


def _to_time_cycle(val: object, _) -> Cycle:
    raise NotImplementedError()


def _to_time_period(val: object, _) -> Period:
    raise NotImplementedError()


def _to_enum(val: object, enum_type: type) -> enum.Enum:
    if isinstance(val, int):
        try:
            return enum_type(val)
        except BaseException:
            raise ValueError(f"Could not parse option ({val}) to an enum ({enum_type})")
    else:
        try:
            return enum_type[str(val)]
        except BaseException:
            try:
                return enum_type[f"_{val}"]
            except BaseException:
                raise ValueError(f"Could not parse value ({val}) to an enum ({enum_type})")


# Map: Type <-> Mapping function.
_VALUE_MAPPERS = {
    Cycle: _to_time_cycle,
    Period: _to_time_period,
    datetime.datetime: lambda val, _: convertor.to_datetime(val),
    datetime.timedelta: lambda val, _: convertor.to_timedelta(val),
    float: lambda val, _: convertor.to_float(val),
    str: lambda val, _: convertor.to_str(val),
} | {i: _to_enum for i in ENUM_SET}
