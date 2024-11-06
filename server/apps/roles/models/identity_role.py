from django.db import models


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

    def __str__(self):
        return self.display_name
