import enum
import typing

from pyactus.codecs.dict_codec import decode as _decode_from_dict
from pyactus.codecs.dict_codec import encode as _encode_to_dict
from pyactus.codecs.json_codec import decode as _decode_from_json
from pyactus.codecs.json_codec import decode as _encode_to_json


class EncodingType(enum.Enum):
    """Enumeration over set of supported encoding formats.

    """
    # Simple python dictionary.
    DICTIONARY = 0

    # JSON string.
    JSON = 1


def decode(encoded: object, entity_type: object, encoding: EncodingType = EncodingType.JSON) -> object:
    """Decodes a domain entity from a serialised representation.

    :param encoded: A domain entity instance encoded in a supported format.
    :param entity_type: Type of domain entity being decoded.
    :param encoding: Type of domain encoding to apply.
    :returns: A decoded domain entity.

    """
    if encoding == EncodingType.DICTIONARY:
        decoder = _decode_from_dict
    elif encoding == EncodingType.JSON:
        decoder = _decode_from_json
    else:
        raise ValueError(f"Unsupported encoding format: {encoding}.")

    if isinstance(encoded, list):
        return [decoder(i, entity_type) for i in encoded]
    else:
        return decoder(encoded, entity_type)


def encode(entity: object, encoding: EncodingType = EncodingType.JSON) -> typing.Union[dict, str]:
    """Encodes a domain entity as a JSON string.

    :param entity: A domain entity instance.
    :param encoding: Type of domain encoding to apply.
    :returns: A domain entity encoded accordingly.

    """
    if encoding == EncodingType.DICTIONARY:
        encoder = _encode_to_dict
    elif encoding == EncodingType.JSON:
        encoder = _encode_to_json
    else:
        raise ValueError("Unsupported encoding format.")

    return encoder(entity)


__all__ = [
    EncodingType,
    decode,
    encode
]
