# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus import core
from pyactus import enums


@dataclasses.dataclass
class FutureTermset(core.ContractTermset):
    """Set of applicable terms: FUTUR -> Future.

    Keeps track of value changes for any basic CT as underlying (PAM, ANN etc. but also FXOUT, STK, COM). Handles margining calls.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.FUTUR

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Clearing House.
    clearing_house: enums.ClearingHouse = None

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Structure.
    contract_structure: typing.List[core.ContractReference] = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Cycle Anchor Date Of Margining.
    cycle_anchor_date_of_margining: datetime.datetime = None

    # Cycle Of Margining.
    cycle_of_margining: core.Cycle = None

    # Delinquency Period.
    delinquency_period: core.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # Delivery Settlement.
    delivery_settlement: enums.DeliverySettlement = enums.DeliverySettlement.D

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Exercise Amount.
    exercise_amount: float = None

    # Exercise Date.
    exercise_date: datetime.datetime = None

    # Futures Price.
    futures_price: float = None

    # Grace Period.
    grace_period: core.Period = None

    # Initial Margin.
    initial_margin: float = None

    # Maintenance Margin Lower Bound.
    maintenance_margin_lower_bound: float = None

    # Maintenance Margin Upper Bound.
    maintenance_margin_upper_bound: float = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Price At Purchase Date.
    price_at_purchase_date: float = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Purchase Date.
    purchase_date: datetime.datetime = None

    # Seniority.
    seniority: enums.Seniority = None

    # Settlement Currency.
    settlement_currency: str = None

    # Settlement Period.
    settlement_period: core.Period = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

    # Variation Margin.
    variation_margin: float = None

