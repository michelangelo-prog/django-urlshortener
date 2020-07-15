from unittest import TestCase

from django.urls import resolve, reverse


class TestRedirect(TestCase):
    def test_redirect(self):
        shortcut = "cb"
        url_shortcut = "/{}".format(shortcut)

        self.assertEqual(url_shortcut, reverse("redirect_to_url", args=(shortcut,)))
        self.assertEqual("redirect_to_url", resolve(url_shortcut).view_name)

    def test_add_url(self):
        self.assertEqual("/", reverse("add_url"))
        self.assertEqual("add_url", resolve("/").view_name)
