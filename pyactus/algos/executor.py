# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import datetime
import typing

from pyactus.algos import algos_of_ann
from pyactus.algos import algos_of_anx
from pyactus.algos import algos_of_bndcp
from pyactus.algos import algos_of_bndwr
from pyactus.algos import algos_of_capfl
from pyactus.algos import algos_of_cdswp
from pyactus.algos import algos_of_cec
from pyactus.algos import algos_of_ceg
from pyactus.algos import algos_of_clm
from pyactus.algos import algos_of_clnte
from pyactus.algos import algos_of_com
from pyactus.algos import algos_of_csh
from pyactus.algos import algos_of_futur
from pyactus.algos import algos_of_fxout
from pyactus.algos import algos_of_lam
from pyactus.algos import algos_of_lax
from pyactus.algos import algos_of_mar
from pyactus.algos import algos_of_nam
from pyactus.algos import algos_of_nax
from pyactus.algos import algos_of_optns
from pyactus.algos import algos_of_pam
from pyactus.algos import algos_of_pbn
from pyactus.algos import algos_of_rep
from pyactus.algos import algos_of_scrcr
from pyactus.algos import algos_of_scrmr
from pyactus.algos import algos_of_stk
from pyactus.algos import algos_of_swaps
from pyactus.algos import algos_of_swppv
from pyactus.algos import algos_of_trswp
from pyactus.algos import algos_of_ump
from pyactus.types.core import ContractTermset
from pyactus.types.core import Event
from pyactus.types.enums import ContractType


# Map: contract type <-> function handle.
_HANDLES = {
    ContractType.ANN: algos_of_ann,
    ContractType.ANX: algos_of_anx,
    ContractType.BNDCP: algos_of_bndcp,
    ContractType.BNDWR: algos_of_bndwr,
    ContractType.CAPFL: algos_of_capfl,
    ContractType.CDSWP: algos_of_cdswp,
    ContractType.CEC: algos_of_cec,
    ContractType.CEG: algos_of_ceg,
    ContractType.CLM: algos_of_clm,
    ContractType.CLNTE: algos_of_clnte,
    ContractType.COM: algos_of_com,
    ContractType.CSH: algos_of_csh,
    ContractType.FUTUR: algos_of_futur,
    ContractType.FXOUT: algos_of_fxout,
    ContractType.LAM: algos_of_lam,
    ContractType.LAX: algos_of_lax,
    ContractType.MAR: algos_of_mar,
    ContractType.NAM: algos_of_nam,
    ContractType.NAX: algos_of_nax,
    ContractType.OPTNS: algos_of_optns,
    ContractType.PAM: algos_of_pam,
    ContractType.PBN: algos_of_pbn,
    ContractType.REP: algos_of_rep,
    ContractType.SCRCR: algos_of_scrcr,
    ContractType.SCRMR: algos_of_scrmr,
    ContractType.STK: algos_of_stk,
    ContractType.SWAPS: algos_of_swaps,
    ContractType.SWPPV: algos_of_swppv,
    ContractType.TRSWP: algos_of_trswp,
    ContractType.UMP: algos_of_ump,
}


def execute_step(
    contract_type: ContractType,
    events: typing.List[Event],
    term_set: ContractTermset,
    observer: object
) -> typing.List[Event]:
    """Applies a set of contract events to the current state of a contract.

    :param events: A list of contract events that should be applied in time sequence.
    :param term_set: The contract's currently applicable set of terms.
    :param observer: The observer for external events & data.
    :returns: The evaluated events and post-event contract states.

    """
    handle = _HANDLES[contract_type]

    return handle.execute_step(events, term_set, observer)


def get_schedule(
    contract_type: ContractType,
    to_date: datetime.datetime,
    term_set: ContractTermset
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


__all__ = [
    execute_step,
    get_schedule
]