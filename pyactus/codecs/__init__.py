from pyactus.codecs.dict_codec import decode as _decode_from_dict
from pyactus.codecs.dict_codec import encode as encode_to_dict
from pyactus.codecs.json_codec import decode as decode_from_json
from pyactus.codecs.json_codec import decode as encode_to_json


def decode_from_dict(encoded: dict, entity_type: object) -> object:
    """Maps information in dictionary format to a type from pyactus.types.

    :param encoded: A dictionary encoded domain entity instance.
    :param entity_type: Type of domain entity being decoded.
    :returns: A decoded domain entity.

    """
    if isinstance(encoded, list):
        return [_decode_from_dict(i, entity_type) for i in encoded]
    else:
        return _decode_from_dict(encoded, entity_type)
