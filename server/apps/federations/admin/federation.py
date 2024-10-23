from ..models import ActiveFederation
from django.contrib import admin


@admin.register(ActiveFederation)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ("url",)
