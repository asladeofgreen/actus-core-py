import dataclasses
import datetime
import typing

from pyactus.types.enums import EventType
from pyactus.types.core.states import StateSpace


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
