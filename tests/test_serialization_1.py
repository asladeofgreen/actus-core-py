import json
import typing

from pyactus import serialisation
from pyactus import typeset


def test_that_a_contract_fixture_is_decodeable(test_contracts: typing.List[dict]):
    for encoded in test_contracts:
        print(encoded)
        decoded = serialisation.from_json(encoded)
        assert decoded.contract_type in typeset.CONTRACT_TERMSETS
        # print(decoded)
        # raise ValueError()
