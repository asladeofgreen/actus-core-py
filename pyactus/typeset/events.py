import dataclasses
import datetime
import enum
import typing

from pyactus.typeset.states import StateSpace


class EventType(enum.Enum):
    """Set of supported contract event types.
    
    """
    # Monitoring :: Monitoring of contract. Evaluates all contract states.
    AD = enum.auto()

    # Initial Exchange :: Scheduled date of initial exchange of e.g. principal value in fixed income products.
    IED = enum.auto()

    # Fee Payment :: Scheduled fee payments.
    FP = enum.auto()

    # Principal Redemption :: Scheduled principal redemption payment.
    PR = enum.auto()

    # Principal Drawing :: Drawing of principal amount e.g. in a credit line.
    PD = enum.auto()

    # Principal Payment Amount Fixing :: Scheduled fixing of principal payment amount.
    PRF = enum.auto()

    # Penalty Payment :: Scheduled payment of a penalty.
    PY = enum.auto()

    # Principal Prepayment :: Unscheduled early repayment of principal.
    PP = enum.auto()

    # Interest Payment :: Scheduled interest payment.
    IP = enum.auto()

    # Interest Capitalization :: Scheduled capitalization of accrued interest.
    IPCI = enum.auto()

    # Credit Event :: Credit event of counterparty to a contract
    CE = enum.auto()

    # Rate Reset Fixing with Known Rate :: Scheduled fixing of variable rate with known new rate.
    RRF = enum.auto()

    # Rate Reset Fixing with Unknown Rate :: Scheduled fixing of variable rate with unknown new rate.
    RR = enum.auto()

    # Dividend Payment :: Payment of dividends.
    DV = enum.auto()

    # Purchase :: Purchase of a contract.
    PRD = enum.auto()

    # Margin Call :: Scheduled margin call.
    MR = enum.auto()

    # Termination :: Termination of a contract.
    TD = enum.auto()

    # Scaling Index Fixing :: Scheduled fixing of a scaling index.
    SC = enum.auto()

    # Interest Calculation Base Fixing :: Scheduled fixing of the interest calculation base.
    IPCB = enum.auto()

    # Maturity :: Maturity of a contract.
    MD = enum.auto()

    # Exercise :: Exercise of a contractual feature such as an optionality.
    XD = enum.auto()

    # Settlement :: Settlement of an exercised contractual claim.
    STD = enum.auto()

    # ???
    PI = enum.auto()

    # Interest Payment FiXed :: interest payment fixed rate events.
    IPFX = enum.auto()

    # Interest Payment Floating Rate :: interest payment floating rate events.
    IPFL = enum.auto()


@dataclasses.dataclass
class Event():
    """Represent a single event generated during the lifetime of a contract.  Such events
    represent the atomic analytical elements comprising all events that possibly
    occur during the lifetime of a contract.  That is, contract events mark specific
    times at which either a state transition, a payoff, or both is generated from a contract.

    Contract events are a generic representation of a specific state transition function and
    pay off function with an event time according to which all events in a contract are ordered
    (in an series) and processed sequentially.  Thereby, processing an event in fact means that 
    it's state transition and payoff functions are evaluated.

    """
    # The Contract ID of the contract which created the event.
    contract_id: str

    # The currency in which the event payoff is scheduled.
    currency: str

    # Time offset within context of an epoch.
    epoch_offset: float

    # The timestamp of the event.
    event_time: datetime.datetime

    # The type of the event. Different types have their own business logic in terms of payoff and state transition functions.
    event_type: EventType

    # The event state-transition function.
    f_state_transition: typing.Callable

    # The event pay-off function.
    f_payoff: typing.Callable

    # The event payoff (if any). Is zero if no payoff needs be settled for the event.
    payoff: float

    # The scheduled timestamp for updating event payoff and post-event state.
    schedule_time: datetime.datetime

    # The post-event state. Results from applying the event’s state transition function to the pre-event state. 
    state: StateSpace
