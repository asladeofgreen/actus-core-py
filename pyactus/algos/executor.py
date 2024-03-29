# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import datetime
import typing

from pyactus.algos import ann as ann_algos
from pyactus.algos import anx as anx_algos
from pyactus.algos import bndcp as bndcp_algos
from pyactus.algos import bndwr as bndwr_algos
from pyactus.algos import capfl as capfl_algos
from pyactus.algos import cdswp as cdswp_algos
from pyactus.algos import cec as cec_algos
from pyactus.algos import ceg as ceg_algos
from pyactus.algos import clm as clm_algos
from pyactus.algos import clnte as clnte_algos
from pyactus.algos import com as com_algos
from pyactus.algos import csh as csh_algos
from pyactus.algos import futur as futur_algos
from pyactus.algos import fxout as fxout_algos
from pyactus.algos import lam as lam_algos
from pyactus.algos import lax as lax_algos
from pyactus.algos import mar as mar_algos
from pyactus.algos import nam as nam_algos
from pyactus.algos import nax as nax_algos
from pyactus.algos import optns as optns_algos
from pyactus.algos import pam as pam_algos
from pyactus.algos import pbn as pbn_algos
from pyactus.algos import rep as rep_algos
from pyactus.algos import scrcr as scrcr_algos
from pyactus.algos import scrmr as scrmr_algos
from pyactus.algos import stk as stk_algos
from pyactus.algos import swaps as swaps_algos
from pyactus.algos import swppv as swppv_algos
from pyactus.algos import trswp as trswp_algos
from pyactus.algos import ump as ump_algos
from pyactus.types.core import ContractTermset
from pyactus.types.core import Event
from pyactus.types.enums import ContractType


# Map: contract type <-> function handle.
_HANDLERS = {
    ContractType.ANN: ann_algos,
    ContractType.ANX: anx_algos,
    ContractType.BNDCP: bndcp_algos,
    ContractType.BNDWR: bndwr_algos,
    ContractType.CAPFL: capfl_algos,
    ContractType.CDSWP: cdswp_algos,
    ContractType.CEC: cec_algos,
    ContractType.CEG: ceg_algos,
    ContractType.CLM: clm_algos,
    ContractType.CLNTE: clnte_algos,
    ContractType.COM: com_algos,
    ContractType.CSH: csh_algos,
    ContractType.FUTUR: futur_algos,
    ContractType.FXOUT: fxout_algos,
    ContractType.LAM: lam_algos,
    ContractType.LAX: lax_algos,
    ContractType.MAR: mar_algos,
    ContractType.NAM: nam_algos,
    ContractType.NAX: nax_algos,
    ContractType.OPTNS: optns_algos,
    ContractType.PAM: pam_algos,
    ContractType.PBN: pbn_algos,
    ContractType.REP: rep_algos,
    ContractType.SCRCR: scrcr_algos,
    ContractType.SCRMR: scrmr_algos,
    ContractType.STK: stk_algos,
    ContractType.SWAPS: swaps_algos,
    ContractType.SWPPV: swppv_algos,
    ContractType.TRSWP: trswp_algos,
    ContractType.UMP: ump_algos,
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
    handler = _HANDLERS[contract_type]

    return handler.execute_step(events, term_set, observer)


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
    handler = _HANDLERS[contract_type]

    return handler.get_schedule(to_date, term_set)


__all__ = [
    execute_step,
    get_schedule
]