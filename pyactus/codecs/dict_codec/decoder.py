from base64 import encode
from pyactus.codecs.utils import dataclass_decoder
from pyactus.codecs.utils import value_convertor as convertor
from pyactus.types.core.contracts import ContractTermset
from pyactus.types.core.events import Event
from pyactus.types.enums import ContractType
from pyactus.types.enums import EventType
from pyactus.types.terms import CONTRACT_TERMSETS


def decode(encoded: dict, typeof: object):
    """Maps information in dictionary format to a type from pyactus.types.

    :param encoded: A dictionary encoded domain entity instance.
    :param entity_type: Type of domain entity being decoded.
    :returns: A decoded domain entity.

    """
    try:
        decoder = _DECODERS[typeof]
    except KeyError:
        raise NotImplementedError(f"Decoding unsupported: entity type={typeof}.")
    else:
        return decoder(encoded)


def _decode_contract_termset(encoded: dict):
    contract_type = ContractType[encoded["contractType"]]
    entity_kls = CONTRACT_TERMSETS[contract_type]

    return dataclass_decoder.decode_entity(encoded, entity_kls)


def _decode_event(encoded: dict):
    return dataclass_decoder.decode_entity(encoded, Event)


_DECODERS = {
    ContractTermset: _decode_contract_termset,
    Event: _decode_event,
}
