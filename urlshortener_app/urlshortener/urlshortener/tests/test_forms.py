import factory
from django.test import TestCase

from ..factories import UrlFactory
from ..forms import UrlForm


class TestUrlForm(TestCase):
    def test_is_valid(self):
        url_data = factory.build(dict, FACTORY_CLASS=UrlFactory)
        form = UrlForm(url_data)
        self.assertTrue(form.is_valid())

    def test_create_url(self):
        url_data = factory.build(dict, FACTORY_CLASS=UrlFactory)
        form = UrlForm(url_data)
        form.save()

        self.assertEqual(url_data["url"], form.data["url"])

    def test_unique_url__validation_in_form_when_pass_existing_url(self):
        url_object = UrlFactory()

        form = UrlForm({"url": url_object.url})

        self.assertFalse(form.is_valid())
        self.assertEqual(1, len(form.errors))
        self.assertTrue(form.has_error("url", "unique"))
        self.assertEqual("Short URL has already been generated.", form.errors["url"][0])

    def test_form_is_not_valid_when_try_to_pass_string_diffrent_than_url_adress(self):
        url_data = factory.build(dict, FACTORY_CLASS=UrlFactory)
        url_data["url"] = "test"
        form = UrlForm(url_data)

        self.assertFalse(form.is_valid())
