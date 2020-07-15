from django.db import models

from .helpers import BASE62IdConverter


class UrlManager(models.Manager):
    def get_by_shortcut(self, shortcut):
        try:
            id = BASE62IdConverter.decode_string_to_id(shortcut)
        except:
            return None
        else:
            return self.filter(id=id).first()
