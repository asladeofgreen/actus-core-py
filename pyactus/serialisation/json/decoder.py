import dataclasses
import datetime
import typing

from pyactus.typeset import CONTRACT_TERMSETS
from pyactus.typeset import ENUM_SET
from pyactus.typeset import Contract
from pyactus.typeset import ContractIdentifier
from pyactus.typeset import ContractLifeCycleEpisode
from pyactus.typeset import ContractReference
from pyactus.typeset import ContractTermset
from pyactus.typeset import ContractType
from pyactus.typeset import Cycle
from pyactus.typeset import Period
from pyactus.typeset import ReferenceRole
from pyactus.typeset import ReferenceType
from pyactus.utils import convertors


# Set of simple scalar types.
_SCALAR_FIELD_TYPES = {
    datetime.datetime,
    float,
    str,
    Cycle,
    Period,
}


def decode(obj: dict) -> object:
    """Maps an Actus contract in dictionary format to it's python type.

    """
    try:
        contract_type: ContractType = ContractType[obj["contract_type"]]
    except KeyError:
        raise ValueError("Invalid contract type")
    else:
        try:
            termset_cls: ContractTermset = CONTRACT_TERMSETS[contract_type]
        except KeyError:
            raise ValueError("Unsupported contract type")

    return Contract(
        contract_type=contract_type,
        identifiers=[_decode_identifier(i) for i in obj["identifiers"]],
        life_cycle=[_decode_life_cycle_episode(i, termset_cls) for i in obj["lifecycle"]]
        )


def _decode_identifier(obj: dict) -> ContractIdentifier:
    """Decodes a contract identifier, e.g. an ITIN.

    """
    return ContractIdentifier(
        scheme=obj["scheme"],
        value=obj["value"]
        )


def _decode_life_cycle_episode(obj: dict, termset_cls: ContractTermset) -> ContractLifeCycleEpisode:
    """Decodes a life cycle episode, i.e. a termset.

    """
    return ContractLifeCycleEpisode(
        term_set=_decode_term_set(obj, termset_cls),
        timestamp=convertors.to_iso_datetime(obj["timestamp"]),
    )


def _decode_term(field, value):
    """Decodes a term value associated with a financial contract.

    """
    if typing.get_origin(field.type) is list:
        value_type = typing.get_args(field.type)[0]
        value = value if isinstance(value, list) else [value]
        return [_decoder(field, i, value_type) for i in value]
    else:
        return _decoder(field, value, field.type)


def _decoder(field, value, value_type):
    if value is None:
        return _decode_term_null_value(field, value, value_type)
    elif value_type in ENUM_SET:
        return _decode_term_enum_value(field, value, value_type)
    elif value_type in _SCALAR_FIELD_TYPES:
        return _decode_term_scalar_value(field, value, value_type)
    elif value_type is ContractReference:
        return _decode_contract_reference(value)

    raise ValueError(f"Unsupported field type: {field.name} :: {field.type} :: {value}") 


def _decode_contract_reference(obj: dict):
    """Decodes a reference to a child financial contract - see structured product.

    """
    print(9999, obj)

    return ContractReference(
        role=ReferenceRole[obj["referenceRole"]],
        typeof=ReferenceType[obj["referenceType"]],
        child=decode(obj["object"])
    )


def _decode_term_1(field, value):
    if typing.get_origin(field.type) is list:
        value_type = typing.get_args(field.type)[0]
        return [_decoder(field, value, value_type) for i in value]
    else:
        return _decoder(field, value, field.type)


def _decode_term_enum_value(field, value, value_type):
    """Decodes a term value when the term type is an enumeration.

    """
    try:
        return value_type[value]
    except KeyError:
        try:
            return value_type[f"_{value}"]
        except KeyError:
            print(f"Unsupported enum value: {field.name} :: {value_type} :: {value}")
            raise ValueError(f"Unsupported enum value: {field.name} :: {value_type} :: {value}")


def _decode_term_null_value(_, value, value_type):
    """Decodes a term value when the term value is null.

    """
    if value_type is float:
        return float(0)

    return None


def _decode_term_scalar_value(field, value, value_type):
    """Decodes a term value when the term type is a scalar.

    """
    if value_type is datetime.datetime:
        return convertors.to_iso_datetime(value)
    elif value_type is float:
        return float(value)
    elif value_type is str:
        return str(value)
    elif value_type is Cycle:
        # print("TODO: convert Cycle: ", field.name, value)
        return value
    elif value_type is Period:
        # print("TODO: convert Period: ", field.name, value)
        return value


def _decode_term_set(obj: dict, termset_cls) -> ContractTermset:
    """Decodes a term set associated with a financial contract.

    """
    # Instantiate termset & map of term fields.
    termset = termset_cls()
    fields = {i.name: i for i in dataclasses.fields(termset_cls)}

    # For each encoded term, map to a field & assign value.
    for name, value in [i.values() for i in obj["term_set"]]:
        name = convertors.to_underscore_case(name)  # format jsonic name as pythonic name 
        try:
            field = fields[name]
        except KeyError:
            print(f"WARNING :: Term name unknown: {termset_cls.__name__} :: {name} :: {value}")
        else:
            # print(field.name, field.type, value, _decode_term(field, value), type(_decode_term(field, value)))
            setattr(termset, name, _decode_term(field, value))

    return termset
