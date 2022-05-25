# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
from pyactus.typeset.enums import ContractType
from pyactus.typeset.terms.annuity import TermsForAnnuity
from pyactus.typeset.terms.cap_floor import TermsForCapFloor
from pyactus.typeset.terms.collateral import TermsForCollateral
from pyactus.typeset.terms.guarantee import TermsForGuarantee
from pyactus.typeset.terms.call_money import TermsForCallMoney
from pyactus.typeset.terms.commodity import TermsForCommodity
from pyactus.typeset.terms.cash import TermsForCash
from pyactus.typeset.terms.future import TermsForFuture
from pyactus.typeset.terms.foreign_exchange_outright import TermsForForeignExchangeOutright
from pyactus.typeset.terms.linear_amortizer import TermsForLinearAmortizer
from pyactus.typeset.terms.exotic_linear_amortizer import TermsForExoticLinearAmortizer
from pyactus.typeset.terms.negative_amortizer import TermsForNegativeAmortizer
from pyactus.typeset.terms.option import TermsForOption
from pyactus.typeset.terms.principal_at_maturity import TermsForPrincipalAtMaturity
from pyactus.typeset.terms.stock import TermsForStock
from pyactus.typeset.terms.swap import TermsForSwap
from pyactus.typeset.terms.plain_vanilla_swap import TermsForPlainVanillaSwap
from pyactus.typeset.terms.undefined_maturity_profile import TermsForUndefinedMaturityProfile


# Set of all supported contract termsets.
CONTRACT_TERMSETS = {
    ContractType.ANN: TermsForAnnuity,
    ContractType.CAPFL: TermsForCapFloor,
    ContractType.CEC: TermsForCollateral,
    ContractType.CEG: TermsForGuarantee,
    ContractType.CLM: TermsForCallMoney,
    ContractType.COM: TermsForCommodity,
    ContractType.CSH: TermsForCash,
    ContractType.FUTUR: TermsForFuture,
    ContractType.FXOUT: TermsForForeignExchangeOutright,
    ContractType.LAM: TermsForLinearAmortizer,
    ContractType.LAX: TermsForExoticLinearAmortizer,
    ContractType.NAM: TermsForNegativeAmortizer,
    ContractType.OPTNS: TermsForOption,
    ContractType.PAM: TermsForPrincipalAtMaturity,
    ContractType.STK: TermsForStock,
    ContractType.SWAPS: TermsForSwap,
    ContractType.SWPPV: TermsForPlainVanillaSwap,
    ContractType.UMP: TermsForUndefinedMaturityProfile,
}