from django.contrib import admin
from django.urls import path
from urlshortener.urlshortener.views import (create_short_url_view,
                                             url_redirect_view)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", view=create_short_url_view, name="add_url"),
    path("<str:shortcut>", view=url_redirect_view, name="redirect_to_url"),
]
