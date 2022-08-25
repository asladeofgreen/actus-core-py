# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
from pyactus.enums import ContractType
from pyactus.terms.ann import AnnuityTermset
from pyactus.terms.anx import ExoticAnnuityTermset
from pyactus.terms.bndcp import ConvertibleNoteTermset
from pyactus.terms.bndwr import WarrantTermset
from pyactus.terms.capfl import CapFloorTermset
from pyactus.terms.cdswp import CreditDefaultSwapTermset
from pyactus.terms.cec import CollateralTermset
from pyactus.terms.ceg import GuaranteeTermset
from pyactus.terms.clm import CallMoneyTermset
from pyactus.terms.clnte import CreditLinkedNoteTermset
from pyactus.terms.com import CommodityTermset
from pyactus.terms.csh import CashTermset
from pyactus.terms.futur import FutureTermset
from pyactus.terms.fxout import ForeignExchangeOutrightTermset
from pyactus.terms.lam import LinearAmortizerTermset
from pyactus.terms.lax import ExoticLinearAmortizerTermset
from pyactus.terms.mar import MarginingTermset
from pyactus.terms.nam import NegativeAmortizerTermset
from pyactus.terms.nax import ExoticNegativeAmortizerTermset
from pyactus.terms.optns import OptionTermset
from pyactus.terms.pam import PrincipalAtMaturityTermset
from pyactus.terms.pbn import PerpetualBondsTermset
from pyactus.terms.rep import RepurchaseAgreementTermset
from pyactus.terms.scrcr import SecuritizationCreditRiskTermset
from pyactus.terms.scrmr import SecuritizationMarketRiskTermset
from pyactus.terms.stk import StockTermset
from pyactus.terms.swaps import SwapTermset
from pyactus.terms.swppv import PlainVanillaSwapTermset
from pyactus.terms.trswp import TotalReturnSwapTermset
from pyactus.terms.ump import UndefinedMaturityProfileTermset


# Map: Contract Type <-> ContractTermset.
CONTRACT_TERMSETS = {
    ContractType.ANN: AnnuityTermset,
    ContractType.ANX: ExoticAnnuityTermset,
    ContractType.BNDCP: ConvertibleNoteTermset,
    ContractType.BNDWR: WarrantTermset,
    ContractType.CAPFL: CapFloorTermset,
    ContractType.CDSWP: CreditDefaultSwapTermset,
    ContractType.CEC: CollateralTermset,
    ContractType.CEG: GuaranteeTermset,
    ContractType.CLM: CallMoneyTermset,
    ContractType.CLNTE: CreditLinkedNoteTermset,
    ContractType.COM: CommodityTermset,
    ContractType.CSH: CashTermset,
    ContractType.FUTUR: FutureTermset,
    ContractType.FXOUT: ForeignExchangeOutrightTermset,
    ContractType.LAM: LinearAmortizerTermset,
    ContractType.LAX: ExoticLinearAmortizerTermset,
    ContractType.MAR: MarginingTermset,
    ContractType.NAM: NegativeAmortizerTermset,
    ContractType.NAX: ExoticNegativeAmortizerTermset,
    ContractType.OPTNS: OptionTermset,
    ContractType.PAM: PrincipalAtMaturityTermset,
    ContractType.PBN: PerpetualBondsTermset,
    ContractType.REP: RepurchaseAgreementTermset,
    ContractType.SCRCR: SecuritizationCreditRiskTermset,
    ContractType.SCRMR: SecuritizationMarketRiskTermset,
    ContractType.STK: StockTermset,
    ContractType.SWAPS: SwapTermset,
    ContractType.SWPPV: PlainVanillaSwapTermset,
    ContractType.TRSWP: TotalReturnSwapTermset,
    ContractType.UMP: UndefinedMaturityProfileTermset,
}
