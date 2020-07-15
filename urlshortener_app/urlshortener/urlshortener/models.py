from django.db import models

from django.conf import settings

from .managers import UrlManager

from .helpers import BASE62IdConverter

from django.urls import reverse


class Url(models.Model):

    object = UrlManager()

    url = models.URLField(max_length=500, unique=True)

    @property
    def short_url(self):
        return "{}{}".format(
            settings.SITE_URL, reverse("redirect_to_url", args=(self.url_shortcut,))
        )

    @property
    def url_shortcut(self):
        return BASE62IdConverter.encode_id_to_string(self.id)

    def __str__(self):
        return "ID: {}, URL: {}".format(self.id, self.url)
