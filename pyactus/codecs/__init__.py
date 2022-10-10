from pyactus.codecs.dict_codec import decode as _decode_from_dict
from pyactus.codecs.dict_codec import encode as _encode_to_dict
from pyactus.codecs.json_codec import decode as _decode_from_json
from pyactus.codecs.json_codec import decode as _encode_to_json


def decode(encoded: object, entity_type: object) -> object:
    """Decodes a domain entity from a serialised representation.

    :param encoded: A domain entity instance encoded in a supported format.
    :param entity_type: Type of domain entity being decoded.
    :returns: A decoded domain entity.

    """
    def _decode(entity: object):
        if isinstance(entity, dict):
            return _decode_from_dict(entity, entity_type)
        elif isinstance(entity, str):
            return _decode_from_json(entity, entity_type)
        else:
            raise ValueError("Unsupported entity encoding format.")

    return [_decode(i) for i in encoded] if isinstance(encoded, list) else _decode(encoded)


def encode(entity: object, entity_type: object) -> object:
    """Encodes a domain entity as a JSON string.

    :param entity: A domain entity instance.
    :returns: A domain entity encoded as a JSON string.

    """
    raise NotImplementedError()


__all__ = [
    decode,
    encode
]
