import datetime
import enum

from pyactus.types.core import Cycle
from pyactus.types.core import Period
from pyactus.types.enums import ENUM_SET
from pyactus.utils.convertors import to_iso_time_interval


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


def to_cycle(val: object, _) -> Cycle:
    """Decodes a domain time cycle from a string representation, e.g. P1ML0.

    """
    val = val.split("L")[0]

    return to_iso_time_interval(val)


def to_datetime(val: str) -> datetime.datetime:
    """Converts an arbitrary value into a datetime representation.

    :param val: An arbitrary value being converted.
    :returns: A datetime representation.

    """
    if val is None:
        return datetime.datetime.utcnow()

    for format in _DATETIME_FORMATS:
        try:
            return datetime.datetime.strptime(val, format)
        except BaseException:
            pass

    raise ValueError(f"Invalid value: cannot parse to a datetime :: {val}")


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
    """Converts an arbitrary value into a float representation.

    :param val: An arbitrary value being converted.
    :returns: A float representation.

    """
    try:
        return float(val)
    except ValueError as err:
        raise err


def to_period(val: object, _) -> Period:
    """Decodes a domain time period from a string representation, e.g. P2D.

    """
    val = val.split("L")[0]

    return to_iso_time_interval(val)


def to_str(val: object) -> str:
    """Converts an arbitrary value into a string representation.

    :param val: An arbitrary value being converted.
    :returns: A string representation.

    """
    try:
        return str(val)
    except ValueError as err:
        raise err


def to_timedelta(val: object) -> datetime.timedelta:
    """Converts an arbitrary value into a timedelta representation.

    :param val: An arbitrary value being converted.
    :returns: A timedelta representation.

    """
    raise NotImplementedError()
