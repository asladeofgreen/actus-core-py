import datetime
import enum

from pyactus.types.core import Cycle
from pyactus.types.core import Period
from pyactus.types.enums import ENUM_SET


# Set of datetime formats aginst which to parse an externally defined date.
_DATETIME_FORMATS = {
    "%Y",
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S"
}


def to_datetime(val: object) -> datetime.datetime:
    if val is None:
        return datetime.datetime.utcnow()

    for format in _DATETIME_FORMATS:
        try:
            return datetime.datetime.strptime(val, format)
        except BaseException:
            pass

    raise ValueError(f"Invalid value: cannot parse to a datetime :: {val}")


def to_time_cycle(val: object) -> Cycle:
    raise NotImplementedError()


def to_time_period(val: object) -> Period:
    raise NotImplementedError()


def to_enum(val: object, enum_type: type) -> enum.Enum:
    """Converts an arbitrary value into an enumeration memeber.
    
    :param val: An arbitrary value being converted.
    :param enum_type: Type of target enum.
    :returns: Pointer to an enum member. 

    """
    if isinstance(val, int):
        try:
            return enum_type(val)
        except BaseException as err:
            raise ValueError(f"Could not parse option ({val}) to an enum ({enum_type})")
    else:
        try:
            return enum_type[str(val)]
        except BaseException as err:
            try:
                return enum_type[f"_{val}"]
            except BaseException as err:
                raise ValueError(f"Could not parse value ({val}) to an enum ({enum_type})")


def to_float(val: object) -> float:
    try:
        return float(val)
    except ValueError as err:
        print(888, val)
        raise err


def to_str(val: object) -> str:
    try:
        return str(val)
    except ValueError as err:
        raise err


def to_timedelta(val: object) -> datetime.timedelta:
    raise NotImplementedError()


# Map: Type <-> Mapping function.
_VALUE_MAPPERS = {
    Cycle: to_time_cycle,
    Period: to_time_period,
    datetime.datetime: to_datetime,
    datetime.timedelta: to_timedelta,
    float: to_float,
    str: to_str
} | {i: to_enum for i in ENUM_SET}
