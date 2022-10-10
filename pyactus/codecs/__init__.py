import enum
import typing

from pyactus.codecs import dict_codec
from pyactus.codecs import json_codec


class EncodingType(enum.Enum):
    """Enumeration over set of supported encoding formats.

    """
    # Simple python dictionary.
    DICTIONARY = 0

    # JSON string.
    JSON = 1


# Map: Encoding type <-> serializer.
_CODECS = {
    EncodingType.DICTIONARY: dict_codec,
    EncodingType.JSON: json_codec,
}


def decode(
    encoded: object,
    typeof: object,
    encoding: EncodingType = EncodingType.JSON
) -> object:
    """Decodes a domain entity from a serialised representation.

    :param encoded: A domain entity instance encoded in a supported format.
    :param typeof: Type of domain entity being decoded.
    :param encoding: Type of domain encoding to apply.
    :returns: A decoded domain entity.

    """
    try:
        codec = _CODECS[encoding]
    except KeyError:
        raise ValueError(f"Unsupported encoding format: {encoding}.")
    else:
        if isinstance(encoded, list):
            return [codec.decode(i, typeof) for i in encoded]
        else:
            return codec.decode(encoded, typeof)


def encode(
    entity: object,
    encoding: EncodingType = EncodingType.JSON
) -> typing.Union[dict, str]:
    """Encodes a domain entity as a JSON string.

    :param entity: A domain entity instance.
    :param encoding: Type of domain encoding to apply.
    :returns: A domain entity encoded accordingly.

    """
    try:
        codec = _CODECS[encoding]
    except KeyError:
        raise ValueError(f"Unsupported encoding format: {encoding}.")
    else:
        return codec.encode(entity)


__all__ = [
    EncodingType,
    decode,
    encode
]
