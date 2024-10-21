from apps.federations.models import ActiveFederation
from django.contrib import admin


@admin.register(ActiveFederation)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ("federation_id", "is_active")
    search_fields = ("federation_id",)
    list_filter = ("is_active",)
