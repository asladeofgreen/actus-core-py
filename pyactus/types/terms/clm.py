# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class CallMoneyTermset(core.ContractTermset):
    """Set of applicable terms: CLM -> Call Money.

    Loans that are rolled over as long as they are not called. Once called it has to be paid back after the stipulated notice period.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CLM

    # Accrued Interest.
    accrued_interest: float = None

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Cycle Anchor Date Of Fee.
    cycle_anchor_date_of_fee: datetime.datetime = None

    # Cycle Anchor Date Of Interest Payment.
    cycle_anchor_date_of_interest_payment: datetime.datetime = None

    # Cycle Anchor Date Of Rate Reset.
    cycle_anchor_date_of_rate_reset: datetime.datetime = None

    # Cycle Of Fee.
    cycle_of_fee: core.Cycle = None

    # Cycle Of Interest Payment.
    cycle_of_interest_payment: core.Cycle = None

    # Cycle Of Rate Reset.
    cycle_of_rate_reset: core.Cycle = None

    # Day Count Convention.
    day_count_convention: enums.DayCountConvention = None

    # Delinquency Period.
    delinquency_period: core.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Fee Accrued.
    fee_accrued: float = None

    # Fee Basis.
    fee_basis: enums.FeeBasis = None

    # Fee Rate.
    fee_rate: float = None

    # Fixing Period.
    fixing_period: core.Period = None

    # Grace Period.
    grace_period: core.Period = None

    # Initial Exchange Date.
    initial_exchange_date: datetime.datetime = None

    # Market Object Code Of Rate Reset.
    market_object_code_of_rate_reset: str = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Next Reset Rate.
    next_reset_rate: float = None

    # Nominal Interest Rate.
    nominal_interest_rate: float = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Notional Principal.
    notional_principal: float = None

    # Prepayment Period.
    prepayment_period: core.Period = None

    # Rate Multiplier.
    rate_multiplier: float = 1.0

    # Rate Spread.
    rate_spread: float = None

    # Seniority.
    seniority: enums.Seniority = None

    # Settlement Currency.
    settlement_currency: str = None

    # Status Date.
    status_date: datetime.datetime = None

    # X Day Notice.
    x_day_notice: core.Period = None

