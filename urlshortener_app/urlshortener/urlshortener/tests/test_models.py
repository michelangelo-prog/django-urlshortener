from django.test import TestCase

import factory

from ..factories import UrlFactory

from ..models import Url

from ..helpers import BASE62IdConverter

from django.db.utils import IntegrityError

from django.conf import settings


class TestLocationModel(TestCase):
    def test_create_url_object(self):
        data = factory.build(dict, FACTORY_CLASS=UrlFactory)

        obj = Url.object.create(**data)

        self.assertEqual(data["url"], obj.url)
        self.assertEqual(
            BASE62IdConverter.encode_id_to_string(obj.id), obj.url_shortcut
        )
        self.assertEqual(
            "{}/{}".format(settings.SITE_URL, obj.url_shortcut), obj.short_url
        )

    def test_raise_exception_when_try_save_same_url_twice(self):
        obj = UrlFactory()

        with self.assertRaises(IntegrityError):
            UrlFactory(url=obj.url)
