import json
import typing

from pyactus.utils import serialisation
from pyactus.types.core import Contract
from pyactus.types.terms import CONTRACT_TERMSETS


def test_that_a_contract_fixture_is_decodeable(test_contracts: typing.List[dict]):
    for encoded in test_contracts:
        print("*" * 120)
        # print(json.dumps(encoded, indent=4))
        decoded: Contract = serialisation.from_json(encoded)
        print(decoded.life_cycle[0])
        # assert decoded.contract_type in CONTRACT_TERMSETS

    raise ValueError()
