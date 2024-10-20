from django.contrib import admin

from apps.federations.models import ActiveFederation


@admin.register(ActiveFederation)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ('federation_id', 'is_active')
    search_fields = ('federation_id',)
    list_filter = ('is_active',)
