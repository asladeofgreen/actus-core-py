# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus import core
from pyactus import enums


@dataclasses.dataclass
class GuaranteeTermset(core.ContractTermset):
    """Set of applicable terms: CEG -> Guarantee.

    Guarantee creates a relationship between a guarantor, an obligee and a debtor, moving the exposure from the debtor to the guarantor.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CEG

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Structure.
    contract_structure: typing.List[core.ContractReference] = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Coverage Of Credit Enhancement.
    coverage_of_credit_enhancement: float = 1.0

    # Creator Identifier.
    creator_id: str = None

    # Credit Event Type Covered.
    credit_event_type_covered: typing.List[enums.CreditEventTypeCovered] = enums.CreditEventTypeCovered.DF

    # Currency.
    currency: str = None

    # Cycle Anchor Date Of Fee.
    cycle_anchor_date_of_fee: datetime.datetime = None

    # Cycle Of Fee.
    cycle_of_fee: core.Cycle = None

    # Delinquency Period.
    delinquency_period: core.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Exercise Amount.
    exercise_amount: float = None

    # Exercise Date.
    exercise_date: datetime.datetime = None

    # Fee Accrued.
    fee_accrued: float = None

    # Fee Basis.
    fee_basis: enums.FeeBasis = None

    # Fee Rate.
    fee_rate: float = None

    # Grace Period.
    grace_period: core.Period = None

    # Guaranteed Exposure.
    guaranteed_exposure: enums.GuaranteedExposure = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Notional Principal.
    notional_principal: float = None

    # Price At Purchase Date.
    price_at_purchase_date: float = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Purchase Date.
    purchase_date: datetime.datetime = None

    # Settlement Currency.
    settlement_currency: str = None

    # Settlement Period.
    settlement_period: core.Period = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

