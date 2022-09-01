# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class OptionTermset(core.ContractTermset):
    """Set of applicable terms: OPTNS -> Option.

    Calculates straight option pay-off for any basic CT as underlying (PAM, ANN etc.) but also SWAPS, FXOUT, STK and COM. Single, periodic and continuous strike is supported.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.OPTNS

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

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Cycle Anchor Date Of Optionality.
    cycle_anchor_date_of_optionality: datetime.datetime = None

    # Cycle Of Optionality.
    cycle_of_optionality: core.Cycle = None

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

    # Grace Period.
    grace_period: core.Period = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Option Exercise End Date.
    option_exercise_end_date: datetime.datetime = None

    # Option Exercise Type.
    option_exercise_type: enums.OptionExerciseType = None

    # Option Strike 1.
    option_strike1: float = None

    # Option Strike 2.
    option_strike2: float = None

    # Option Type.
    option_type: enums.OptionType = None

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

