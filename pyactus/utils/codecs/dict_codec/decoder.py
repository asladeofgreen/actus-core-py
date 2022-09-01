import dataclasses
import datetime
import typing

from pyactus.types.core import Contract
from pyactus.types.core import ContractIdentifier
from pyactus.types.core import ContractReference
from pyactus.types.core import ContractTermset
from pyactus.types.core import Cycle
from pyactus.types.core import Event
from pyactus.types.core import LifeCycleEpisode
from pyactus.types.core import Period
from pyactus.types.core import SCALAR_TERM_VALUE_TYPESET
from pyactus.types.enums import ContractType
from pyactus.types.enums import EventType
from pyactus.types.enums import ReferenceRole
from pyactus.types.enums import ReferenceType
from pyactus.types.enums import ENUM_SET
from pyactus.types.terms import CONTRACT_FIELDSETS
from pyactus.types.terms import CONTRACT_TERMSETS
from pyactus.utils import convertors


def decode(obj: dict) -> object:
    """Maps an Actus contract in dictionary format to it's python type.

    :param obj: An ACTUS contract in an at rest representation.
    :returns: A decoded ACTUS domain entity.

    """
    # TODO: handle other 
    return decode_contract(obj)


def decode_contract(obj: dict) -> Contract:
    try:
        contract_type: ContractType = ContractType[obj["contract_type"]]
    except KeyError:
        raise ValueError(f"Invalid contract type: {obj}")
    else:
        try:
            termset_cls: ContractTermset = CONTRACT_TERMSETS[contract_type]
        except KeyError:
            raise ValueError(f"Unsupported contract type: {contract_type}")

    return Contract(
        contract_type=contract_type,
        identifiers=[_decode_contract_identifier(i) for i in obj["identifiers"]],
        life_cycle=[_decode_life_cycle_episode(i, termset_cls) for i in obj["lifecycle"]]
        )

def _decode_contract_identifier(obj: dict) -> ContractIdentifier:
    return ContractIdentifier(
        scheme=obj["scheme"],
        value=obj["value"]
        )

def _decode_contract_reference(obj: dict) -> ContractReference:
    return ContractReference(
        role=ReferenceRole[obj["referenceRole"]],
        typeof=ReferenceType[obj["referenceType"]],
        child=decode(obj["object"])
    )

def _decode_event(obj: dict) -> Event:
    return Event(
        contract_id=None,
        currency=obj["currency"],
        epoch_offset=float(obj.get("epochOffset", 0.0)),
        event_timestamp=_parse_timestamp(obj.get("eventDate")),
        event_type=EventType[obj["eventType"]],
        f_state_transition=None,
        f_payoff=None,
        payoff=float(obj.get("payoff", 0.0)),
        schedule_time=_parse_timestamp(obj.get("scheduleDate")),
        state=None
    )

def _decode_life_cycle_episode(obj: dict, termset_cls: ContractTermset) -> LifeCycleEpisode:
    return LifeCycleEpisode(
        event_sequence=[_decode_event(i) for i in obj.get("event_sequence", [])],
        event_sequence_proof=obj.get("event_sequence_proof"),
        term_set=_decode_term_set(obj, termset_cls),
        timestamp=convertors.to_iso_datetime(obj["timestamp"]),
    )

def _decode_term(field, value):
    def _decode_enum_value(val, val_type):
        try:
            return val_type[val]
        except KeyError:
            try:
                return val_type[f"_{val}"]
            except KeyError:
                print(f"Unsupported enum value: {field.name} :: {val_type} :: {val}")
                raise ValueError(f"Unsupported enum value: {field.name} :: {val_type} :: {val}")

    def _decode_null_value(val_type):
        if val_type is float:
            return float(0)
        return None

    def _decode_scalar_value(val, val_type):
        if val_type is datetime.datetime:
            return convertors.to_iso_datetime(val)
        elif val_type is float:
            return float(val)
        elif val_type is str:
            return str(val)
        elif val_type is Cycle:
            # print("TODO: convert Cycle: ", field.name, value)
            return val
        elif val_type is Period:
            # print("TODO: convert Period: ", field.name, value)
            return val

    def _decoder(val, val_type):
        if val is None:
            return _decode_null_value(val_type)
        elif val_type in ENUM_SET:
            return _decode_enum_value(val, val_type)
        elif val_type in SCALAR_TERM_VALUE_TYPESET:
            return _decode_scalar_value(val, val_type)
        elif val_type is ContractReference:
            return _decode_contract_reference(val)

        raise ValueError(f"Unsupported field type: {field.name} :: {field.type} :: {val}") 

    if typing.get_origin(field.type) is list:
        value_type = typing.get_args(field.type)[0]
        value = value if isinstance(value, list) else [value]
        return [_decoder(i, value_type) for i in value]
    else:
        return _decoder(value, field.type)

def _decode_term_set(obj: dict, termset_cls: typing.Type) -> ContractTermset:
    # Instantiate termset.
    termset = termset_cls()

    # Set map of term fields.
    try:
        fieldset = CONTRACT_FIELDSETS[termset_cls]
    except KeyError:
        raise ValueError("Termset type cannot be mapped to a field set.")

    # For each term, map to a field & assign value.
    for name, value in [i.values() for i in obj["term_set"]]:
        name = convertors.to_underscore_case(name)  # format jsonic name as pythonic name 
        try:
            field = fieldset[name]
        except KeyError:
            print(f"WARNING :: Term name unknown: {termset_cls.__name__} :: {name} :: {value}")
        else:
            # print(field.name, field.type, value, _decode_term(field, value), type(_decode_term(field, value)))
            setattr(termset, name, _decode_term(field, value))

    return termset

def _parse_timestamp(as_str: str) -> datetime.datetime:
    return datetime.datetime.utcnow()
