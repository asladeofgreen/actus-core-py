import typing

import pytest

from pyactus import algos
from pyactus import codecs
from pyactus.types.terms import ContractTermset
from pyactus.types.terms import CONTRACT_TERMSETS


def test_that_a_contract_event_sequence_can_be_calculated(test_contracts: typing.List[dict]):
    for contract_type, fixture in test_contracts:
        event_sequence = []
        termset = codecs.decode_from_dict(fixture["terms"], ContractTermset)
        with pytest.raises(KeyError):
            algos.execute_step(contract_type, event_sequence, termset, None)
