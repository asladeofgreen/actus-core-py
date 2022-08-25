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
class Swap(contracts.ContractTermset)Termset:
    """Set of applicable terms: SWAPS -> Swap.

    Exchange of two basic CT´s (PAM, ANN etc.). Normally one is fixed, the other variable. However all variants possible including different currencies for cross currency swaps, basic swaps or even different principal exchange programs.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.SWAPS

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Contract Structure.
    contract_structure: typing.List[contracts.ContractReference] = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Delinquency Period.
    delinquency_period: auxiliary.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # Delivery Settlement.
    delivery_settlement: enums.DeliverySettlement = enums.DeliverySettlement.D

    # Grace Period.
    grace_period: auxiliary.Period = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

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

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

