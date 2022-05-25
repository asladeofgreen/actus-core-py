import dataclasses
import datetime
import typing
import uuid

from pyactus.typeset.enums import ContractType
from pyactus.typeset.events import Event



@dataclasses.dataclass
class ContractTerms():
    """A set of terms associated with a specific type of contract.
    
    NOTE: this is subclassed in pyactus.typeset.termsets.{contract-type}.py.
    """
    pass


@dataclasses.dataclass
class CalculationProof():
    """Encapsulates information related to a cryptographic calculation proof.

    """
    # Timestamp at which calcuation was performed.
    timestamp: datetime.datetime


@dataclasses.dataclass
class LifeCycleEpisode():
    """Encapsulates information related to episodes in  a contract life cycle.

    """
    # Set of applicable terms.
    term_set: ContractTerms

    # Sequence of events emitted by a calculation engine.
    event_sequence: typing.List[Event] = list

    # Proof of event sequence calculation.
    event_sequence_proof: CalculationProof = None

    # Timestamp at which life cycle event occurred.
    timestamp: datetime.datetime = datetime.datetime.utcnow

    # Information related to external event that triggered life cycle event.
    trigger: str = "issuance"

    # Universally unique identifier.
    uid: str = uuid.uuid4

    def __str__(self) -> str:
        return f"lifecycle-episode|{self.term_set.contract_type}|{self.timestamp}|{self.uid}"


@dataclasses.dataclass
class ContractIdentifier():
    """Encapsulates information required by a system to uniquely identify a contract.
    
    """
    # Identifier scheme, e.g. ISIN.
    scheme: str

    # Identifier value, e.g. DE000XXB2UL2.
    value: str


@dataclasses.dataclass
class Contract():
    """An ACTUS compliant financial contract agreed upon by a set of counter-parties.
    
    """
    # ACTUS contract type.
    contract_type: ContractType

    # Associated identifiers.
    identifiers: typing.List[ContractIdentifier]

    # Life cycle history of terms & events.
    life_cycle: typing.List[LifeCycleEpisode]

    # Universally unique identifier.
    uid: str = str(uuid.uuid4())
