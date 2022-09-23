import typing

def test_that_test_contracts_can_be_read_from_fsys(test_contracts: typing.List[dict]):
    for fixture in test_contracts:
        assert isinstance(fixture, dict)
        for key in {"contract_type", "identifiers", "lifecycle", "uid"}:
            assert key in fixture
