from multiprocessing.sharedctypes import Value
import typing

import pytest

from pyactus import algos
from pyactus import codecs
from pyactus.types.core import ContractTermset
from pyactus.types.enums import ContractType
from pyactus.types.terms import CONTRACT_TERMSETS


def test_that_a_contract_event_sequence_can_be_calculated(test_contracts: typing.List[dict]):
    for contract_type, fixture in test_contracts:
        if contract_type != ContractType.ANN:
            continue

        termset = codecs.decode(fixture["terms"], ContractTermset)

        event_sequence = []
        algos.execute_step(contract_type, event_sequence, termset, None)


    raise ValueError()
