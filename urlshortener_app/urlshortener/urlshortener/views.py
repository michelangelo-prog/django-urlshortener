from django.views.generic import CreateView, RedirectView
from .forms import UrlForm

from .models import Url

from django.http import Http404


class CreateShortUrlView(CreateView):

    template_name = "urlshortener/urlshortener_view.html"
    form_class = UrlForm

    def form_valid(self, form):
        self.object = form.save()
        context = self.get_context_data()
        context["short_url"] = self.object.short_url
        return self.render_to_response(context)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        if form.has_error("url", "unique"):
            url_object = Url.object.get(url=form.data["url"])
            context["short_url"] = url_object.short_url
        else:
            context.pop("short_url", None)
        return self.render_to_response(context)


create_short_url_view = CreateShortUrlView.as_view()


class UrlRedirectView(RedirectView):

    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        shortcut = kwargs.get("shortcut")
        object = Url.object.get_by_shortcut(shortcut)
        if object:
            return object.url
        else:
            raise Http404


url_redirect_view = UrlRedirectView.as_view()
