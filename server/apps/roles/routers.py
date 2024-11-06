from apps.roles.viewsets import IdentityRoleViewSet
from rest_framework import routers

roles_router = routers.DefaultRouter()

roles_router.register(
    prefix="",
    viewset=IdentityRoleViewSet,
    basename="roles",
)
