import dataclasses
import datetime
import typing
import uuid

from pyactus.enums import ContractType
from pyactus.enums import ReferenceRole
from pyactus.enums import ReferenceType
from pyactus.core.events import Event



@dataclasses.dataclass
class ContractExecutionProof():
    """Encapsulates information related to a proof of calculation correctness.

    """
    # Timestamp at which calcuation was performed.
    timestamp: datetime.datetime


@dataclasses.dataclass
class ContractIdentifier():
    """Encapsulates information required by a system to uniquely identify a contract.

    """
    # Identifier scheme, e.g. ISIN.
    scheme: str

    # Identifier value, e.g. DE000XXB2UL2.
    value: str


@dataclasses.dataclass
class ContractLifeCycleEpisode():
    """Encapsulates information related to episodes in  a contract life cycle.

    """
    # Set of applicable terms.
    term_set: "ContractTermset"

    # Sequence of events emitted by a calculation engine.
    event_sequence: typing.List[Event] = list

    # Proof of event sequence calculation.
    event_sequence_proof: ContractExecutionProof = None

    # Timestamp at which life cycle event occurred.
    timestamp: datetime.datetime = datetime.datetime.utcnow().isoformat

    # Information related to external event that triggered life cycle event.
    trigger: str = "issuance"

    # Universally unique identifier.
    uid: str = uuid.uuid4

    def __str__(self) -> str:
        return f"lifecycle-episode|{self.term_set.contract_type}|{self.timestamp}|{self.uid}"


@dataclasses.dataclass
class ContractReference():
    """An ACTUS compliant financial contract agreed upon by a set of counter-parties.

    """
    # Role of reference in respect of parent contract.
    role: ReferenceRole

    # Type of reference in respect of parent contract.
    typeof: ReferenceType

    # Actual child contract.
    child: "Contract"


@dataclasses.dataclass
class ContractTermset():
    """A set of terms associated with a specific type of contract.

    NOTE: this is subclassed in pyactus.typeset.termsets.{contract-type}.py.
    """
    pass


@dataclasses.dataclass
class Contract():
    """An ACTUS compliant financial contract agreed upon by a set of counter-parties.

    """
    # ACTUS contract type.
    contract_type: ContractType

    # Associated identifiers.
    identifiers: typing.List[ContractIdentifier]

    # Life cycle history of terms & events.
    life_cycle: typing.List[ContractLifeCycleEpisode]

    # Universally unique identifier.
    uid: str = str(uuid.uuid4())
