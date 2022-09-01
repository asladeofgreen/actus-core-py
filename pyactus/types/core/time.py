import datetime
import typing


# Time cycle.
Cycle = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)

# Time period.
Period = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)
