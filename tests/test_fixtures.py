import typing

from pyactus.types.enums import ContractType


def test_that_test_contracts_can_be_read_from_fsys(test_contracts: typing.List[dict]):
    for fixture in test_contracts:
        assert isinstance(fixture, tuple)
        assert len(fixture) == 2
        assert isinstance(fixture[0], ContractType)
        for key in {"contract_id", "contract_type", "event_sequence", "observed_data", "terms"}:
            assert key in fixture[1]
