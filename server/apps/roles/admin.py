from django.contrib import admin

from .models import IdentityRole


@admin.register(IdentityRole)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ("display_name", "entity_type", "is_active")
