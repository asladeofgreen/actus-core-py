# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus import core
from pyactus import enums


@dataclasses.dataclass
class PlainVanillaSwapTermset(core.ContractTermset):
    """Set of applicable terms: SWPPV -> Plain Vanilla Swap.

    Plain vanilla swaps where the underlyings are always two identical PAM´s however with one leg fixed and the other variable.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.SWPPV

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

    # Cycle Anchor Date Of Interest Payment.
    cycle_anchor_date_of_interest_payment: datetime.datetime = None

    # Cycle Anchor Date Of Rate Reset.
    cycle_anchor_date_of_rate_reset: datetime.datetime = None

    # Cycle Of Interest Payment.
    cycle_of_interest_payment: core.Cycle = None

    # Cycle Of Rate Reset.
    cycle_of_rate_reset: core.Cycle = None

    # Cycle Point Of Rate Reset.
    cycle_point_of_rate_reset: enums.CyclePointOfRateReset = enums.CyclePointOfRateReset.B

    # Day Count Convention.
    day_count_convention: enums.DayCountConvention = None

    # Delinquency Period.
    delinquency_period: core.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # Delivery Settlement.
    delivery_settlement: enums.DeliverySettlement = enums.DeliverySettlement.D

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Fixing Period.
    fixing_period: core.Period = None

    # Grace Period.
    grace_period: core.Period = None

    # Initial Exchange Date.
    initial_exchange_date: datetime.datetime = None

    # Market Object Code.
    market_object_code: str = None

    # Market Object Code Of Rate Reset.
    market_object_code_of_rate_reset: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Next Reset Rate.
    next_reset_rate: float = None

    # Nominal Interest Rate.
    nominal_interest_rate: float = None

    # Nominal Interest Rate 2.
    nominal_interest_rate2: float = None

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

    # Termination Date.
    termination_date: datetime.datetime = None

