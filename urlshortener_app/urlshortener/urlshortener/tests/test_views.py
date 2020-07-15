from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse

from ..factories import UrlFactory
from ..views import create_short_url_view


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

    def test_return_404_when_url_not_exists_in_db(self):
        test_url_shortcut = "testtesttest"
        response = self.client.get(
            reverse("redirect_to_url", args=(test_url_shortcut,)), follow=True
        )

        self.assertEqual(404, response.status_code)


class CreateShortUrlView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_view(self):
        request = self.factory.get("/")
        request.user = AnonymousUser()
        response = create_short_url_view(request)
        self.assertEqual(200, response.status_code)
