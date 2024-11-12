from apps.entity_types import ENTITY_TYPE_CHOICES_DJANGO
from django.conf import settings
from django.db import models


class IdentityRole(models.Model):
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPE_CHOICES_DJANGO)
    is_active = models.BooleanField(default=False)
    display_name = models.CharField(max_length=50)
    logo_image = models.ImageField(upload_to="identity_roles/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_identity_roles",
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="updated_identity_roles",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.display_name
