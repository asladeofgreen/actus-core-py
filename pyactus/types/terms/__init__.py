# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses

from pyactus.types.enums import ContractType
from pyactus.types.terms.ann import AnnuityTermset
from pyactus.types.terms.anx import ExoticAnnuityTermset
from pyactus.types.terms.bndcp import ConvertibleNoteTermset
from pyactus.types.terms.bndwr import WarrantTermset
from pyactus.types.terms.capfl import CapFloorTermset
from pyactus.types.terms.cdswp import CreditDefaultSwapTermset
from pyactus.types.terms.cec import CollateralTermset
from pyactus.types.terms.ceg import GuaranteeTermset
from pyactus.types.terms.clm import CallMoneyTermset
from pyactus.types.terms.clnte import CreditLinkedNoteTermset
from pyactus.types.terms.com import CommodityTermset
from pyactus.types.terms.csh import CashTermset
from pyactus.types.terms.futur import FutureTermset
from pyactus.types.terms.fxout import ForeignExchangeOutrightTermset
from pyactus.types.terms.lam import LinearAmortizerTermset
from pyactus.types.terms.lax import ExoticLinearAmortizerTermset
from pyactus.types.terms.mar import MarginingTermset
from pyactus.types.terms.nam import NegativeAmortizerTermset
from pyactus.types.terms.nax import ExoticNegativeAmortizerTermset
from pyactus.types.terms.optns import OptionTermset
from pyactus.types.terms.pam import PrincipalAtMaturityTermset
from pyactus.types.terms.pbn import PerpetualBondsTermset
from pyactus.types.terms.rep import RepurchaseAgreementTermset
from pyactus.types.terms.scrcr import SecuritizationCreditRiskTermset
from pyactus.types.terms.scrmr import SecuritizationMarketRiskTermset
from pyactus.types.terms.stk import StockTermset
from pyactus.types.terms.swaps import SwapTermset
from pyactus.types.terms.swppv import PlainVanillaSwapTermset
from pyactus.types.terms.trswp import TotalReturnSwapTermset
from pyactus.types.terms.ump import UndefinedMaturityProfileTermset

# Map: contract type <-> contract field set.
CONTRACT_FIELDSETS = {
    AnnuityTermset: {i.name: i for i in dataclasses.fields(AnnuityTermset)},
    ExoticAnnuityTermset: {i.name: i for i in dataclasses.fields(ExoticAnnuityTermset)},
    ConvertibleNoteTermset: {i.name: i for i in dataclasses.fields(ConvertibleNoteTermset)},
    WarrantTermset: {i.name: i for i in dataclasses.fields(WarrantTermset)},
    CapFloorTermset: {i.name: i for i in dataclasses.fields(CapFloorTermset)},
    CreditDefaultSwapTermset: {i.name: i for i in dataclasses.fields(CreditDefaultSwapTermset)},
    CollateralTermset: {i.name: i for i in dataclasses.fields(CollateralTermset)},
    GuaranteeTermset: {i.name: i for i in dataclasses.fields(GuaranteeTermset)},
    CallMoneyTermset: {i.name: i for i in dataclasses.fields(CallMoneyTermset)},
    CreditLinkedNoteTermset: {i.name: i for i in dataclasses.fields(CreditLinkedNoteTermset)},
    CommodityTermset: {i.name: i for i in dataclasses.fields(CommodityTermset)},
    CashTermset: {i.name: i for i in dataclasses.fields(CashTermset)},
    FutureTermset: {i.name: i for i in dataclasses.fields(FutureTermset)},
    ForeignExchangeOutrightTermset: {i.name: i for i in dataclasses.fields(ForeignExchangeOutrightTermset)},
    LinearAmortizerTermset: {i.name: i for i in dataclasses.fields(LinearAmortizerTermset)},
    ExoticLinearAmortizerTermset: {i.name: i for i in dataclasses.fields(ExoticLinearAmortizerTermset)},
    MarginingTermset: {i.name: i for i in dataclasses.fields(MarginingTermset)},
    NegativeAmortizerTermset: {i.name: i for i in dataclasses.fields(NegativeAmortizerTermset)},
    ExoticNegativeAmortizerTermset: {i.name: i for i in dataclasses.fields(ExoticNegativeAmortizerTermset)},
    OptionTermset: {i.name: i for i in dataclasses.fields(OptionTermset)},
    PrincipalAtMaturityTermset: {i.name: i for i in dataclasses.fields(PrincipalAtMaturityTermset)},
    PerpetualBondsTermset: {i.name: i for i in dataclasses.fields(PerpetualBondsTermset)},
    RepurchaseAgreementTermset: {i.name: i for i in dataclasses.fields(RepurchaseAgreementTermset)},
    SecuritizationCreditRiskTermset: {i.name: i for i in dataclasses.fields(SecuritizationCreditRiskTermset)},
    SecuritizationMarketRiskTermset: {i.name: i for i in dataclasses.fields(SecuritizationMarketRiskTermset)},
    StockTermset: {i.name: i for i in dataclasses.fields(StockTermset)},
    SwapTermset: {i.name: i for i in dataclasses.fields(SwapTermset)},
    PlainVanillaSwapTermset: {i.name: i for i in dataclasses.fields(PlainVanillaSwapTermset)},
    TotalReturnSwapTermset: {i.name: i for i in dataclasses.fields(TotalReturnSwapTermset)},
    UndefinedMaturityProfileTermset: {i.name: i for i in dataclasses.fields(UndefinedMaturityProfileTermset)},
}

# Map: contract type <-> contract term set.
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
