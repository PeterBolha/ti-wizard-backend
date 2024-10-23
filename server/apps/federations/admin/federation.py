from django.contrib import admin

from ..models import ActiveFederation


@admin.register(ActiveFederation)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ("url",)
