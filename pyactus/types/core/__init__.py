import datetime

from pyactus.types.core.contracts import Contract
from pyactus.types.core.contracts import ContractExecutionProof
from pyactus.types.core.contracts import ContractIdentifier
from pyactus.types.core.contracts import LifeCycleEpisode
from pyactus.types.core.contracts import ContractReference
from pyactus.types.core.contracts import ContractTermset
from pyactus.types.core.events import Event
from pyactus.types.core.funcs import PayoffFunction
from pyactus.types.core.funcs import StateTransitionFunction
from pyactus.types.core.states import StateSpace
from pyactus.types.core.time import Cycle
from pyactus.types.core.time import Period


# Set of simple scalar types.
SCALAR_TERM_VALUE_TYPESET = {
    datetime.datetime,
    float,
    str,
    Cycle,
    Period,
}
