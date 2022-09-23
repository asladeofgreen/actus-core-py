import typing

from pyactus import codecs
from pyactus.types.core import Event
from pyactus.types.terms import ContractTermset
from pyactus.types.terms import CONTRACT_TERMSETS


def test_that_contract_termsets_can_be_decoded_from_a_dictionary(test_contracts: typing.List[dict]):
    for contract_type, fixture in test_contracts:
        encoded = fixture["terms"]
        decoded = codecs.decode_from_dict(encoded, ContractTermset)
        assert isinstance(decoded, CONTRACT_TERMSETS[contract_type])


def test_that_event_sequences_can_be_decod_from_a_dictionaryed(test_contracts: typing.List[dict]):
    for contract_type, fixture in test_contracts:
        encoded: typing.List[dict] = fixture["event_sequence"]
        decoded: typing.List[Event] = codecs.decode_from_dict(encoded, Event)
        assert isinstance(decoded, list)
        assert len(decoded) == len(encoded)
        for item in decoded:
            assert isinstance(item, Event)
