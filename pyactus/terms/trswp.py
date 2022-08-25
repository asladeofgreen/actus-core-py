# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.typeset import enums
from pyactus.typeset import auxiliary
from pyactus.typeset import contracts


@dataclasses.dataclass
class TotalReturnSwap(contracts.ContractTermset)Termset:
    """Set of applicable terms: TRSWP -> Total Return Swap.

    A total return swap is a swap agreement in which one party makes payments based on a set rate, either fixed or variable, while the other party makes payments based on the return of an underlying asset, which includes both the income it generates and any capital gains.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.TRSWP

    # WARNING:: This contract type has not yet been formally defined.  This class is thus simply a placeholder.
    # raise NotImplementedError("WARNING: Standard does not yet support this contract type.")
