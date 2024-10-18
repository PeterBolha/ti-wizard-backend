from django.urls import path
from . import views
from .views import SamlSp, SamlIdp

urlpatterns = [
    path("", views.index, name="index"),
    path("oidc/op", views.oidc_op, name="oidc-op"),
    path("oidc/rp", views.oidc_rp, name="oidc-rp"),
    path("saml/idp", SamlIdp.as_view(), name="saml-idp"),
    path("saml/sp", SamlSp.as_view(), name="saml-sp"),
]