from django.db import models
from django.conf import settings


class IdentityRole(models.Model):
    # entity_type should be one of 4 options: SAML_IDP...
    ENTITY_TYPE_CHOICES = [
        ('SAML_IDP', 'SAML IDP'),
        ('SAML_SP', 'SAML SP'),
        ('OIDC_OP', 'OIDC OP'),
        ('OIDC_RP', 'OIDC RP'),
    ]

    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPE_CHOICES)
    is_active = models.BooleanField(default=False)
    display_name = models.CharField(max_length=50)
    logo_image = models.ImageField(upload_to='identity_roles/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_identity_roles',
                                   on_delete=models.SET_NULL, null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_identity_roles',
                                   on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.display_name
