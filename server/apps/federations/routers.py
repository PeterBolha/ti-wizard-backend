from rest_framework import routers

from .viewsets import FederationViewSet

federations_router = routers.DefaultRouter()

federations_router.register(
    prefix='',
    viewset=FederationViewSet,
    basename='federations',
)
