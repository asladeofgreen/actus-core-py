# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
from pyactus.typeset.enums import ContractType
from pyactus.typeset.termsets.annuity import TermsetOfAnnuity
from pyactus.typeset.termsets.exotic_annuity import TermsetOfExoticAnnuity
from pyactus.typeset.termsets.convertible_note import TermsetOfConvertibleNote
from pyactus.typeset.termsets.warrant import TermsetOfWarrant
from pyactus.typeset.termsets.cap_floor import TermsetOfCapFloor
from pyactus.typeset.termsets.credit_default_swap import TermsetOfCreditDefaultSwap
from pyactus.typeset.termsets.collateral import TermsetOfCollateral
from pyactus.typeset.termsets.guarantee import TermsetOfGuarantee
from pyactus.typeset.termsets.call_money import TermsetOfCallMoney
from pyactus.typeset.termsets.credit_linked_note import TermsetOfCreditLinkedNote
from pyactus.typeset.termsets.commodity import TermsetOfCommodity
from pyactus.typeset.termsets.cash import TermsetOfCash
from pyactus.typeset.termsets.future import TermsetOfFuture
from pyactus.typeset.termsets.foreign_exchange_outright import TermsetOfForeignExchangeOutright
from pyactus.typeset.termsets.linear_amortizer import TermsetOfLinearAmortizer
from pyactus.typeset.termsets.exotic_linear_amortizer import TermsetOfExoticLinearAmortizer
from pyactus.typeset.termsets.margining import TermsetOfMargining
from pyactus.typeset.termsets.negative_amortizer import TermsetOfNegativeAmortizer
from pyactus.typeset.termsets.exotic_negative_amortizer import TermsetOfExoticNegativeAmortizer
from pyactus.typeset.termsets.option import TermsetOfOption
from pyactus.typeset.termsets.principal_at_maturity import TermsetOfPrincipalAtMaturity
from pyactus.typeset.termsets.perpetual_bonds import TermsetOfPerpetualBonds
from pyactus.typeset.termsets.repurchase_agreement import TermsetOfRepurchaseAgreement
from pyactus.typeset.termsets.securitization_credit_risk import TermsetOfSecuritizationCreditRisk
from pyactus.typeset.termsets.securitization_market_risk import TermsetOfSecuritizationMarketRisk
from pyactus.typeset.termsets.stock import TermsetOfStock
from pyactus.typeset.termsets.swap import TermsetOfSwap
from pyactus.typeset.termsets.plain_vanilla_swap import TermsetOfPlainVanillaSwap
from pyactus.typeset.termsets.total_return_swap import TermsetOfTotalReturnSwap
from pyactus.typeset.termsets.undefined_maturity_profile import TermsetOfUndefinedMaturityProfile


# Set of all supported contract termsets.
CONTRACT_TERMSETS = {
    ContractType.ANN: TermsetOfAnnuity,
    ContractType.ANX: TermsetOfExoticAnnuity,
    ContractType.BNDCP: TermsetOfConvertibleNote,
    ContractType.BNDWR: TermsetOfWarrant,
    ContractType.CAPFL: TermsetOfCapFloor,
    ContractType.CDSWP: TermsetOfCreditDefaultSwap,
    ContractType.CEC: TermsetOfCollateral,
    ContractType.CEG: TermsetOfGuarantee,
    ContractType.CLM: TermsetOfCallMoney,
    ContractType.CLNTE: TermsetOfCreditLinkedNote,
    ContractType.COM: TermsetOfCommodity,
    ContractType.CSH: TermsetOfCash,
    ContractType.FUTUR: TermsetOfFuture,
    ContractType.FXOUT: TermsetOfForeignExchangeOutright,
    ContractType.LAM: TermsetOfLinearAmortizer,
    ContractType.LAX: TermsetOfExoticLinearAmortizer,
    ContractType.MAR: TermsetOfMargining,
    ContractType.NAM: TermsetOfNegativeAmortizer,
    ContractType.NAX: TermsetOfExoticNegativeAmortizer,
    ContractType.OPTNS: TermsetOfOption,
    ContractType.PAM: TermsetOfPrincipalAtMaturity,
    ContractType.PBN: TermsetOfPerpetualBonds,
    ContractType.REP: TermsetOfRepurchaseAgreement,
    ContractType.SCRCR: TermsetOfSecuritizationCreditRisk,
    ContractType.SCRMR: TermsetOfSecuritizationMarketRisk,
    ContractType.STK: TermsetOfStock,
    ContractType.SWAPS: TermsetOfSwap,
    ContractType.SWPPV: TermsetOfPlainVanillaSwap,
    ContractType.TRSWP: TermsetOfTotalReturnSwap,
    ContractType.UMP: TermsetOfUndefinedMaturityProfile,
}
