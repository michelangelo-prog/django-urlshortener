from django.contrib import admin
from django.utils.html import format_html

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    fields = (
        "pk",
        "url",
        "show_short_url",
    )
    readonly_fields = (
        "pk",
        "show_short_url",
    )
    ordering = ("pk",)

    def show_short_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.short_url)

    show_short_url.short_description = "Short URL"


admin.site.register(Url, UrlAdmin)
