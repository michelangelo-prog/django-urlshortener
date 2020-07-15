from unittest import TestCase

from ..helpers import BASE62IdConverter


class TestBASE62IdConverter(TestCase):
    def test_encode_id_to_string(self):
        id = 125
        result = BASE62IdConverter.encode_id_to_string(id)
        expected_string = "21"
        self.assertEqual(expected_string, result)

    def test_decode_string_to_id(self):
        string = "21"
        result = BASE62IdConverter.decode_string_to_id(string)
        expected_id = 125
        self.assertEqual(expected_id, result)
