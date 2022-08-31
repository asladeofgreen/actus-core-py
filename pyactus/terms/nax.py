# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus import core
from pyactus import enums


@dataclasses.dataclass
class ExoticNegativeAmortizerTermset(core.ContractTermset):
    """Set of applicable terms: NAX -> Exotic Negative Amortizer.

    Exotic version of NAM However step ups with respect to (i) Principal, (ii) Interest rates are possible. Highly flexible to match totally irregular principal payments. Principal can also be paid out in steps.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.NAX

    # WARNING:: This contract type has not yet been formally defined.  This class is thus simply a placeholder.
    # raise NotImplementedError("WARNING: Standard does not yet support this contract type.")
