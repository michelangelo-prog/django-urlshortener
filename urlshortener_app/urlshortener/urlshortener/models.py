from django.db import models

from .managers import UrlManager

from .helpers import BASE62IdConverter

class Url(models.Model):

    object = UrlManager()

    url = models.URLField(max_length=500, unique=True)

    @property
    def short_url(self):
        return BASE62IdConverter.encode_id_to_string(self.id)

    def __str__(self):
        return "ID: {}, URL: {}".format(self.id, self.url)