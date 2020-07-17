from factory import Sequence
from factory.django import DjangoModelFactory

from .models import Url


class UrlFactory(DjangoModelFactory):
    class Meta:
        model = Url

    url = Sequence(lambda n: f"http://localhost/test/test{n}")
