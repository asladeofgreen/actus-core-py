# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.typeset import enums
from pyactus.typeset import auxiliary
from pyactus.typeset import contracts


@dataclasses.dataclass
class TermsetOfForeignExchangeOutright(contracts.ContractTermset):
    """Set of applicable terms: FXOUT -> Foreign Ex-change Outright.

    Two parties agree to exchange two fixed cash flows in different currencies at a certain point in time in future.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.FXOUT

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

    # Currency 2.
    currency2: str = None

    # Delinquency Period.
    delinquency_period: auxiliary.Period = None

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

    # Grace Period.
    grace_period: auxiliary.Period = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Notional Principal.
    notional_principal: float = None

    # Notional Principal 2.
    notional_principal2: float = None

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
    settlement_period: auxiliary.Period = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

