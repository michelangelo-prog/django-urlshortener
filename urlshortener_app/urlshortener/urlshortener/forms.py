from django import forms

from .models import Url

class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = [ "url" ]

    url = forms.URLField(error_messages={"unique":"Short URL has already been generated."})