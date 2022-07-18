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
class TermsetOfSecuritizationCreditRisk(contracts.ContractTermset):
    """Set of applicable terms: SCRCR -> Securitization Credit Risk.

    Securitiazion contracts where contracs are ranked according to credit default. The lower ranked tranches are hit by the first defaults. Only when the lowest tranches are wiped out, the next higher tranch is hit.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.SCRCR

    # WARNING:: This contract type has not yet been formally defined.  This class is thus simply a placeholder.
    # raise NotImplementedError("WARNING: Standard does not yet support this contract type.")
