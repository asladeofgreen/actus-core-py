from pyactus.codecs.utils import dataclass_decoder
from pyactus.types.core.contracts import ContractTermset
from pyactus.types.core.events import Event
from pyactus.types.enums import ContractType
from pyactus.types.terms import CONTRACT_TERMSETS


def decode(encoded: dict, typeof: object):
    """Maps information in dictionary format to a type from pyactus.types.

    :param encoded: A dictionary encoded domain entity instance.
    :param typeof: Type of domain entity being decoded.
    :returns: A decoded domain entity.

    """
    try:
        decoder = _DECODERS[typeof]
    except KeyError:
        raise NotImplementedError(f"Decoding unsupported: entity type={typeof}.")
    else:
        return decoder(encoded)


def _decode_contract_termset(encoded: dict):
    """Decodes a contract termset from a simple python dictionary.
    
    """
    contract_type = ContractType[encoded["contractType"]]
    entity_kls = CONTRACT_TERMSETS[contract_type]

    return dataclass_decoder.decode_entity(encoded, entity_kls)


def _decode_event(encoded: dict):
    """Decodes a contract event from a simple python dictionary.
    
    """
    return dataclass_decoder.decode_entity(encoded, Event)


# Map: Domain entity type <-> Decoding function.
_DECODERS = {
    ContractTermset: _decode_contract_termset,
    Event: _decode_event,
}
