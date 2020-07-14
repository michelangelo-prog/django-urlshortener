from django.test import TestCase

from ..factories import UrlFactory

from ..models import Url

from ..helpers import BASE62IdConverter

class TestUrlManager(TestCase):
    def setUp(self):
        self.url_objs = [UrlFactory() for i in range(100)]

    def test_get_by_shortcut(self):
        received_url_obj = [Url.object.get_by_shortcut(obj.short_url) for obj in self.url_objs]

        for get_obj, expected_obj in zip(received_url_obj, self.url_objs):
            self.assertEqual(expected_obj.id, get_obj.id)

    def test_get_by_shortcut_return__none__when_obj_does_not_exist(self):
        latest_id = Url.object.last().id
        not_existed_id = latest_id + 1
        not_existed_id_short_url = BASE62IdConverter.encode_id_to_string(not_existed_id)

        self.assertIsNone(Url.object.get_by_shortcut(not_existed_id_short_url))