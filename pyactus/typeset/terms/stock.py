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
class TermsForStock(contracts.ContractTerms):
    """Set of applicable terms: STK -> Stock.

    Any instrument which is bought at a certain amount (market price normally) and then follows an index.

    """
    # Business Day Convention :: 
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar :: 
    calendar: enums.Calendar = enums.Calendar.NC

    # Contract Deal Date :: 
    contract_deal_date: datetime.datetime = None

    # Contract Identifier :: 
    contract_id: str = None

    # Contract Performance :: 
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Role :: 
    contract_role: enums.ContractRole = None

    # Counterparty Identifier :: 
    counterparty_id: str = None

    # Creator Identifier :: 
    creator_id: str = None

    # Currency :: 
    currency: str = None

    # Cycle Anchor Date Of Dividend :: 
    cycle_anchor_date_of_dividend: datetime.datetime = None

    # Cycle Of Dividend :: 
    cycle_of_dividend: auxiliary.Cycle = None

    # End Of Month Convention :: 
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Ex Dividend Date :: 
    ex_dividend_date: datetime.datetime = None

    # Market Object Code :: 
    market_object_code: str = None

    # Market Value Observed :: 
    market_value_observed: float = None

    # Next Dividend Payment Amount :: 
    next_dividend_payment_amount: float = 'TODO: format 0'

    # Non Performing Date :: 
    non_performing_date: datetime.datetime = None

    # Notional Principal :: 
    notional_principal: float = None

    # Price At Purchase Date :: 
    price_at_purchase_date: float = None

    # Price At Termination Date :: 
    price_at_termination_date: float = None

    # Purchase Date :: 
    purchase_date: datetime.datetime = None

    # Quantity :: 
    quantity: float = 'TODO: format 1'

    # Seniority :: 
    seniority: enums.Seniority = None

    # Settlement Currency :: 
    settlement_currency: str = None

    # Status Date :: 
    status_date: datetime.datetime = None

    # Termination Date :: 
    termination_date: datetime.datetime = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.STK