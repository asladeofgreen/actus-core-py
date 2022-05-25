import datetime
import json
import os
import pathlib
import typing
import uuid

import pytest

from pyactus.typeset import ContractType


# Path to test assets folder.
_ASSETS: pathlib.Path = pathlib.Path(os.path.dirname(__file__)).parent / "assets"


@pytest.fixture(scope="session")
def test_contracts():
    """Returns set of test contract fixtures. 
    
    """
    return list(_yield_contracts())


def _yield_contracts() -> typing.Iterator[typing.Tuple[ContractType, dict]]:
    """Yields set of test contract fixtures. 
    
    """
    for contract_type in ContractType:
        if contract_type != ContractType.PAM:
            continue
        for obj in _read_contract_fixtures(contract_type):
            yield _map_contract_fixture(contract_type, obj)


def _read_contract_fixtures(contract_type: ContractType) -> typing.List[dict]:
    """Reads an official ACTUS text fixture into memory.
    
    """
    fpath: pathlib.Path = _ASSETS / f"actus-tests-{contract_type.name.lower()}.json"
    if not fpath.exists():
        return []

    with open(fpath, "r") as fstream:
        return json.loads(fstream.read()).values()


def _map_contract_fixture(contract_type: ContractType, obj: dict) -> dict:
    """Maps a test contract fixture to it's over the wire ACTUS representation.
    
    """
    def _map_term_set():
        return [
            { "name": k, "value": v} 
            for k, v in sorted(obj["terms"].items(), key=lambda i: i[0]) 
            if k not in {"contractID", "contractType"}
            ]

    return {
        "contract_type": contract_type.name,
        "identifiers": [
            {
                "value": obj["terms"]["contractID"],
                "scheme": "test-framework",
            }
        ],
        "lifecycle": [
            {
                "event_sequence": obj["results"],
                "event_sequence_proof": None,
                "term_set": _map_term_set(),
                "timestamp": datetime.datetime.utcnow(),
                "trigger": None,
            }
        ],
        "uid": str(uuid.uuid4())
    }
