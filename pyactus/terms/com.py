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
class Commodity(contracts.ContractTermset)Termset:
    """Set of applicable terms: COM -> Commodity.

    This is not a financial contract in its propper sense. However it traks movements of commodities such as oil, gas or even houses. Such commodities can serve as underlyings of commodity futures, guarantees or simply asset positions.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.COM

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Market Object Code.
    market_object_code: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Price At Purchase Date.
    price_at_purchase_date: float = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Purchase Date.
    purchase_date: datetime.datetime = None

    # Quantity.
    quantity: float = 1.0

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

    # Unit.
    unit: enums.Unit = None

