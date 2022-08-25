# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ArrayIncreaseDecrease(enum.Enum):
    """ARINCDEC :: Array Increase Decrease.

    Indicates whether a certain PRNXT element in ARPRNX increases the principal (NT) or decreases it.Applies only for ANX, NAX, LAX Maturity CTs. For all other Maturity CTs the first principal payment is always in the opposite direction of all other (following) payments.

    """
    # Increase :: Notional is increased in this period.
    INC = 0

    # Decrease :: Notional is decreased in this period.
    DEC = 1

