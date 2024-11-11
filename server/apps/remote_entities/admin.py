from django.contrib import admin

from .models import RemoteEntity


@admin.register(RemoteEntity)
class ActiveFederationAdmin(admin.ModelAdmin):
    list_display = ("name", "entity_type", "is_active")

    # forbid editing of these fields
    readonly_fields = ("id", "created_at", "updated_at", "created_by", "updated_by")
