from django.test import TestCase
from django.urls import reverse

from ..factories import UrlFactory


class TestUrlRedirectView(TestCase):
    def test_redirect_to_url(self):
        url_obj = UrlFactory()

        response = self.client.get(
            reverse("redirect_to_url", args=(url_obj.url_shortcut,)), follow=True
        )

        self.assertRedirects(
            response,
            url_obj.url,
            status_code=301,
            target_status_code=404,
            fetch_redirect_response=True,
        )

    def test_raise_404_when_url_not_exists_in_db(self):
        test_url_shortcut = "testtesttest"
        response = self.client.get(
            reverse("redirect_to_url", args=(test_url_shortcut,)), follow=True
        )

        self.assertEqual(404, response.status_code)
