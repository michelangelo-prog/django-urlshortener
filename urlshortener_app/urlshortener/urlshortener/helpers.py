from django.utils import baseconv


class BASE62IdConverter:
    @classmethod
    def encode_id_to_string(cls, number):
        return baseconv.base62.encode(number)

    @classmethod
    def decode_string_to_id(cls, string):
        return baseconv.base62.decode(string)
