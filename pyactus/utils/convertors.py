import datetime
import re


def to_camel_case(name: str, separator: str ='_'):
    """Converts passed name to camel case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to camel case.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def to_interest_rate(val: str) -> float:
    """Converts passed value to an interest rate.

    :returns: An interest rate.

    """
    return float(val) / 100


def to_iso_datetime(val: str) -> datetime.datetime:
    """Converts passed value to an ISO date time.

    :param val: A character encoded representation of an ISO date time.
    :returns: An ISO compliant datetime.

    """
    return datetime.datetime.fromisoformat(val)


def to_iso_datetime_T00(val: str):
    """Converts passed value to an ISO date time with time set to 00:00:00.000.

    :param val: A character encoded representation of an ISO date time.
    :returns: An ISO compliant datetime.

    """
    return to_iso_datetime(val).replace(hour=0, minute=0, second=0, microsecond=0)


def to_iso_datetime_T24(val: str):
    """Converts passed value to an ISO date time with time set to 23:59:59.000.

    :param val: A character encoded representation of an ISO date time.
    :returns: An ISO compliant datetime.

    """
    return to_iso_datetime(val).replace(hour=23, minute=59, second=59, microsecond=0)


def to_pascal_case(name: str, separator: str ='_'):
    """Converts passed name to pascal case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to pascal case.

    """
    r = ''
    s = to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def to_underscore_case(target: str):
    """Helper function to convert a from camel case string to an underscore case string.

    :param target: A string for conversion.
    :returns: A string converted to underscore case, e.g. account_number.

    """
    if target is None or not len(target):
        return ''

    r = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', target)
    r = re.sub('([a-z0-9])([A-Z])', r'\1_\2', r)
    r = r.lower()

    return r
