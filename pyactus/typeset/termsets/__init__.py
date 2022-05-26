# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
from pyactus.typeset.enums import ContractType
from pyactus.typeset.termsets.annuity import TermsetOfAnnuity
from pyactus.typeset.termsets.cap_floor import TermsetOfCapFloor
from pyactus.typeset.termsets.collateral import TermsetOfCollateral
from pyactus.typeset.termsets.guarantee import TermsetOfGuarantee
from pyactus.typeset.termsets.call_money import TermsetOfCallMoney
from pyactus.typeset.termsets.commodity import TermsetOfCommodity
from pyactus.typeset.termsets.cash import TermsetOfCash
from pyactus.typeset.termsets.future import TermsetOfFuture
from pyactus.typeset.termsets.foreign_exchange_outright import TermsetOfForeignExchangeOutright
from pyactus.typeset.termsets.linear_amortizer import TermsetOfLinearAmortizer
from pyactus.typeset.termsets.exotic_linear_amortizer import TermsetOfExoticLinearAmortizer
from pyactus.typeset.termsets.negative_amortizer import TermsetOfNegativeAmortizer
from pyactus.typeset.termsets.option import TermsetOfOption
from pyactus.typeset.termsets.principal_at_maturity import TermsetOfPrincipalAtMaturity
from pyactus.typeset.termsets.stock import TermsetOfStock
from pyactus.typeset.termsets.swap import TermsetOfSwap
from pyactus.typeset.termsets.plain_vanilla_swap import TermsetOfPlainVanillaSwap
from pyactus.typeset.termsets.undefined_maturity_profile import TermsetOfUndefinedMaturityProfile


# Set of all supported contract termsets.
CONTRACT_TERMSETS = {
    ContractType.ANN: TermsetOfAnnuity,
    ContractType.CAPFL: TermsetOfCapFloor,
    ContractType.CEC: TermsetOfCollateral,
    ContractType.CEG: TermsetOfGuarantee,
    ContractType.CLM: TermsetOfCallMoney,
    ContractType.COM: TermsetOfCommodity,
    ContractType.CSH: TermsetOfCash,
    ContractType.FUTUR: TermsetOfFuture,
    ContractType.FXOUT: TermsetOfForeignExchangeOutright,
    ContractType.LAM: TermsetOfLinearAmortizer,
    ContractType.LAX: TermsetOfExoticLinearAmortizer,
    ContractType.NAM: TermsetOfNegativeAmortizer,
    ContractType.OPTNS: TermsetOfOption,
    ContractType.PAM: TermsetOfPrincipalAtMaturity,
    ContractType.STK: TermsetOfStock,
    ContractType.SWAPS: TermsetOfSwap,
    ContractType.SWPPV: TermsetOfPlainVanillaSwap,
    ContractType.UMP: TermsetOfUndefinedMaturityProfile,
}
