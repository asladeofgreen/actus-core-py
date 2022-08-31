# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus import core
from pyactus import enums


@dataclasses.dataclass
class CreditLinkedNoteTermset(core.ContractTermset):
    """Set of applicable terms: CLNTE -> Credit Linked Note.

    A credit linked note is a security with an embedded CDSWP

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CLNTE

    # WARNING:: This contract type has not yet been formally defined.  This class is thus simply a placeholder.
    # raise NotImplementedError("WARNING: Standard does not yet support this contract type.")
