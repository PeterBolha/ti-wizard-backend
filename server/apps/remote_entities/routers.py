from apps.remote_entities.viewsets import RemoteEntityViewSet
from rest_framework import routers

remote_entities_router = routers.DefaultRouter()

remote_entities_router.register(
    prefix="",
    viewset=RemoteEntityViewSet,
    basename="remote-entities",
)
