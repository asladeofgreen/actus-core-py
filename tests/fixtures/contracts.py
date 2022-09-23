import datetime
import json
import os
import pathlib
import typing
import uuid

import pytest

from pyactus.types.enums import ContractType


# Path to test assets folder.
_ASSETS: pathlib.Path = pathlib.Path(os.path.dirname(__file__)).parent / "assets"


@pytest.fixture(scope="session")
def test_contracts() -> typing.List[typing.Tuple[ContractType, dict]]:
    """Returns set of test contract fixtures.

    """
    return list(_yield_contracts())


def _yield_contracts() -> typing.Iterator[typing.Tuple[ContractType, dict]]:
    """Yields set of test contract fixtures.

    """
    for contract_type in ContractType:
        for obj in _read_fixtures(contract_type):
            if "contractType" not in obj:
                obj["contractType"] = contract_type.name            
            yield contract_type, _map_fixture(contract_type, obj)


def _read_fixtures(contract_type: ContractType) -> typing.List[dict]:
    """Reads an official ACTUS text fixture into memory.

    """
    fname: str = f"actus-tests-{contract_type.name.lower()}.json"
    fpath: pathlib.Path = _ASSETS / fname
    if not fpath.exists():
        return []

    with open(fpath, "r") as fstream:
        return json.loads(fstream.read()).values()


def _map_fixture(contract_type: ContractType, obj: dict) -> dict:
    """Maps a test contract fixture to it's over the wire ACTUS representation.

    """
    def _map_event(obj: dict):
        obj["eventTimestamp"] = obj["eventDate"]
        return obj

    def _map_term_set():
        def _map_name(name):
            if name == "fixingDays":
                return "fixingPeriod"
            return name

        def _map_value(name, value):
            if name == "arrayFixedVariable" and isinstance(value, list):
                return [i[0] for i in value]
            if name == "calendar" and value == "NOCALENDAR":
                return "NC"
            return value

        return {_map_name(k): _map_value(k, v) for k, v in obj["terms"].items()}

    return {
        "contract_id": obj["terms"]["contractID"],
        "contract_type": contract_type.name,
        "event_sequence": [_map_event(i) for i in obj["results"]],
        "observed_data": obj["dataObserved"],
        "terms": _map_term_set()
    }
