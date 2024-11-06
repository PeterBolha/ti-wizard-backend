from rest_framework import routers

from apps.roles.viewsets import IdentityRoleViewSet

roles_router = routers.DefaultRouter()

roles_router.register(
    prefix="",
    viewset=IdentityRoleViewSet,
    basename="roles",
)

