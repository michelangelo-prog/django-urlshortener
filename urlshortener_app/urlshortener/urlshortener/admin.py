from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
    fields = ("pk", "url", "short_url",)
    readonly_fields = ("pk", "short_url",)
    ordering = ("pk",)

admin.site.register(Url, UrlAdmin)