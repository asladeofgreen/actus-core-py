# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ScalingEffect(enum.Enum):
    """SCEF :: Scaling Effect.

    Indicates which payments are scaled. I = Interest payments, N = Nominal payments and M = Maximum deferred interest amount. They can be scaled in any combination.

    """
    # No Scaling :: No scaling applies.
    OOO = 0

    # Interest is Scaled :: Scaling applies only to interest.
    IOO = 1

    # Principal is Scaled :: Scaling applies only to principal.
    ONO = 2

    # Interest and Principal is Scaled :: Scaling applies to interest and principal.
    INO = 3

