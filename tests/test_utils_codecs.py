import typing

from pyactus.utils import codecs
from pyactus.types.core import Contract


def test_that_a_contract_fixture_is_decodeable(test_contracts: typing.List[dict]):
    for encoded in test_contracts:
        print("*" * 120)
        # print(json.dumps(encoded, indent=4))
        entity: Contract = codecs.from_dict(encoded)
        # assert encoded == codecs.to_dict(entity)


        # assert decoded.contract_type in CONTRACT_TERMSETS

    raise ValueError()
