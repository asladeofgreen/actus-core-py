import json
import typing

from pyactus.utils import serialisation
from pyactus.types.terms import CONTRACT_TERMSETS


def test_that_a_contract_fixture_is_decodeable(test_contracts: typing.List[dict]):
    for encoded in test_contracts:
        print(encoded)
        decoded = serialisation.from_json(encoded)
        assert decoded.contract_type in CONTRACT_TERMSETS
        # print(decoded)
        # raise ValueError()
