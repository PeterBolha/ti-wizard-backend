import hashlib

from apps.entity_types import ENTITY_TYPE_CHOICES, ENTITY_TYPE_CHOICES_DJANGO
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


def get_sha256_hash(data_to_hash: str) -> str:
    return hashlib.sha256(data_to_hash.encode("utf-8")).hexdigest()


def generate_id_hash(entity_type: str, entity_id: str = "", client_id: str = "") -> str:
    if entity_type.startswith("SAML"):
        return get_sha256_hash(entity_id)

    if entity_type.startswith("OIDC"):
        return get_sha256_hash(client_id)

    return ""


class RemoteEntity(models.Model):
    name = models.TextField(blank=True, default="")
    description = models.TextField(blank=True, default="")
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPE_CHOICES_DJANGO)

    # SAML IDP required fields
    entity_id = models.TextField(blank=True, default="")
    metadata_url = models.TextField(blank=True, default="")

    # OIDC OP required fields
    discovery_url = models.TextField(blank=True, default="")

    # OIDC RP required fields
    client_id = models.TextField(blank=True, default="")
    client_secret = models.TextField(blank=True, default="")
    redirect_uri = models.TextField(blank=True, default="")
    dynamic_registration = models.BooleanField(default=False)

    # SHA256 hash of either entity id for SAML entities or client id for OIDC entities to provide
    # a uniform identifier shared amongst all the system components
    id_hash = models.CharField(max_length=64, unique=True, blank=False, null=False)

    is_active = models.BooleanField(default=False)
    comment = models.TextField(blank=True, default="")
    metadata_hash = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_remote_entity",
        on_delete=models.SET_NULL,
        null=True,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="updated_remote_entity",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.name} ({self.entity_type})"

    def clean(self):
        if self.entity_type in ["SAML_IDP", "SAML_SP"]:
            if not self.entity_id:
                raise ValidationError(
                    {
                        "entity_id": f"Entity ID must be set for "
                        f"{ENTITY_TYPE_CHOICES[self.entity_type]}"
                    }
                )

            if not self.metadata_url:
                raise ValidationError(
                    {
                        "metadata_url": f"Metadata URL mus"
                        f"t be set for {ENTITY_TYPE_CHOICES[self.entity_type]}"
                    }
                )

        elif self.entity_type == "OIDC OP":
            if not self.discovery_url:
                raise ValidationError(
                    {
                        "discovery_url": f"Discovery URL "
                        f"must be set for {ENTITY_TYPE_CHOICES[self.entity_type]}"
                    }
                )

        elif self.entity_type == "OIDC_RP":
            if not self.redirect_uri:
                raise ValidationError(
                    {
                        "redirect_uri": f"Redirect URI"
                        f" must be set for {ENTITY_TYPE_CHOICES[self.entity_type]}"
                    }
                )

            if not self.dynamic_registration:
                if not self.client_id:
                    raise ValidationError(
                        {
                            "client_id": f"OIDC Client ID must be set for "
                            f"{ENTITY_TYPE_CHOICES[self.entity_type]} when dynamic "
                            f"registration is not available."
                        }
                    )

                if not self.client_secret:
                    raise ValidationError(
                        {
                            "client_secret": f"Client secret must be set for OIDC Client secret "
                            f"must be set for "
                            f"{ENTITY_TYPE_CHOICES[self.entity_type]} when dynamic"
                            f" registration is not available."
                        }
                    )

        else:
            raise ValidationError(
                {
                    "entity_type": f"Unknown entity type: '{self.entity_type}' Entity type must "
                    f"be one of "
                    f"{list(ENTITY_TYPE_CHOICES.keys())}"
                }
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.id_hash:
            self.id_hash = generate_id_hash(
                str(self.entity_type), str(self.entity_id), str(self.client_id)
            )
        super().save(*args, **kwargs)
