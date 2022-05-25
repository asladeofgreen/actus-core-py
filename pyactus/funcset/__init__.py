# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import datetime
import typing

from pyactus.funcset import ann
from pyactus.funcset import capfl
from pyactus.funcset import cec
from pyactus.funcset import ceg
from pyactus.funcset import clm
from pyactus.funcset import com
from pyactus.funcset import csh
from pyactus.funcset import futur
from pyactus.funcset import fxout
from pyactus.funcset import lam
from pyactus.funcset import lax
from pyactus.funcset import nam
from pyactus.funcset import optns
from pyactus.funcset import pam
from pyactus.funcset import stk
from pyactus.funcset import swaps
from pyactus.funcset import swppv
from pyactus.funcset import ump
from pyactus.typeset import ContractTerms
from pyactus.typeset import ContractType
from pyactus.typeset import Event


# Map: contract type <-> function handle.
_HANDLES = {
    ContractType.ANN: ann,
    ContractType.CAPFL: capfl,
    ContractType.CEC: cec,
    ContractType.CEG: ceg,
    ContractType.CLM: clm,
    ContractType.COM: com,
    ContractType.CSH: csh,
    ContractType.FUTUR: futur,
    ContractType.FXOUT: fxout,
    ContractType.LAM: lam,
    ContractType.LAX: lax,
    ContractType.NAM: nam,
    ContractType.OPTNS: optns,
    ContractType.PAM: pam,
    ContractType.STK: stk,
    ContractType.SWAPS: swaps,
    ContractType.SWPPV: swppv,
    ContractType.UMP: ump,
}


def execute_step(
    contract_type: ContractType,
    events: typing.List[Event],
    terms: ContractTerms,
    observer: object
) -> typing.List[Event]:
    """Applies a set of contract events to the current state of a contract.

    :param events: A list of contract events that should be applied in time sequence.
    :param terms: The contract's currently applicable set of terms.
    :param observer: The observer for external events & data.
    :returns: The evaluated events and post-event contract states.

    """
    handle = _HANDLES[contract_type]

    return handle.execute_step(events, terms, observer)


def get_schedule(
    to_date: datetime.datetime,
    term_set: ContractTerms
) -> typing.List[Event]:
    """Evaluates next contract event sequence within a certain time period.

    The set of contract attributes are mapped to the stream of next contract events
    within a specified time period according to the legal logic of the respective 
    Contract Type and contingent to the risk factor dynamics provided with the
    risk factor model.  The contract's status date is used as the reference time
    as from which the code period is evaluated.

    Note, the stream of the next non-contingent contract events matches the portion
    of the stream of the next contingent events up to the first contingent event.
    Furthermore, for a contract with purely non-contingent events
    (e.g. a PrincipalAtMaturity without a RateReset, Scaling, CreditDefault, etc.) 
    contingent and non-contingent event streams are the same.

    :param to_date: The time up to which the events are to be evaluated.
    :param term_set: The contract term set.
    :returns: An event sequence upto to_date.

    """
    handle = _HANDLES[contract_type]

    return handle.get_schedule(to_date, term_set)