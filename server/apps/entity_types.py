# entity_type should be one of 4 options: SAML_IDP...
# dict format for easier separate extraction of keys and values
ENTITY_TYPE_CHOICES = {
    "SAML_IDP": "SAML IDP",
    "SAML_SP": "SAML SP",
    "OIDC_OP": "OIDC OP",
    "OIDC_RP": "OIDC RP",
}

# tuple format required for django ORM constraint definition
ENTITY_TYPE_CHOICES_DJANGO = [
    (actual_val_key, human_readable_name_val)
    for actual_val_key, human_readable_name_val in ENTITY_TYPE_CHOICES.items()
]
