from factory.django import DjangoModelFactory
from factory import Sequence

from .models import Url


class UrlFactory(DjangoModelFactory):
    class Meta:
        model = Url

    url = Sequence(lambda n: f"http://test.pl/test{n}")
