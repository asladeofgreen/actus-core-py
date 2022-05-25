# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ArrayFixedVariable(enum.Enum):
    """ARFIXVAR :: Array Fixed Variable.

    For array-type rate reset schedules, this attributes defines the meaning of ARRATE.

    """
    # Fixed Rate :: Rate spread represents a fixed rate.
    F = 0

    # Variable Rate :: Rate spread represents the spread on top of a reference rate.
    V = 1

