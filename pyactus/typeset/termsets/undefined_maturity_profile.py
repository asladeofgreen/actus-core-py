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
class TermsetOfUndefinedMaturityProfile(contracts.ContractTermset):
    """Set of applicable terms: UMP -> Undefined Maturity Profile.

    Principal paid in and out at any point in time without prefixed schedule. Interest calculated on outstanding and capitalized periodically. Needs link to a behavioral function describing expected flows.

    """
    # Accrued Interest.
    accrued_interest: float = None

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Identifier.
    contract_id: str = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Role.
    contract_role: enums.ContractRole = None

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
    cycle_of_fee: auxiliary.Cycle = None

    # Cycle Of Interest Payment.
    cycle_of_interest_payment: auxiliary.Cycle = None

    # Cycle Of Rate Reset.
    cycle_of_rate_reset: auxiliary.Cycle = None

    # Day Count Convention.
    day_count_convention: enums.DayCountConvention = None

    # Delinquency Period.
    delinquency_period: auxiliary.Period = None

    # Delinquency Rate.
    delinquency_rate: float = 'TODO: format 0'

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Fee Accrued.
    fee_accrued: float = None

    # Fee Basis.
    fee_basis: enums.FeeBasis = None

    # Fee Rate.
    fee_rate: float = None

    # Grace Period.
    grace_period: auxiliary.Period = None

    # Initial Exchange Date.
    initial_exchange_date: datetime.datetime = None

    # Market Object Code Of Rate Reset.
    market_object_code_of_rate_reset: str = None

    # Maximum Penalty Free Disbursement.
    maximum_penalty_free_disbursement: float = 'TODO: format [ the value of notionalPrincipal ]'

    # Nominal Interest Rate.
    nominal_interest_rate: float = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Notional Principal.
    notional_principal: float = None

    # Prepayment Period.
    prepayment_period: auxiliary.Period = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Rate Spread.
    rate_spread: float = 'TODO: format 0'

    # Seniority.
    seniority: enums.Seniority = None

    # Settlement Currency.
    settlement_currency: str = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

    # X Day Notice.
    x_day_notice: auxiliary.Period = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.UMP
