from pyactus.types.enums import ContractType


def test_contract_set(test_contracts):
    for fixture in test_contracts:
        assert isinstance(fixture, dict)
        for key in {"contract_type", "identifiers", "lifecycle", "uid"}:
            assert key in fixture
