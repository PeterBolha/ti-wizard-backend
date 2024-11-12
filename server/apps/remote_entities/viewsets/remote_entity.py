from typing import Final

from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, serializers, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated

from ..models import RemoteEntity
from ..serializers import RemoteEntitySerializer, RemoteEntityUpdateStatusSerializer


@method_decorator(
    name="create",
    decorator=extend_schema(
        tags=["remote-entities"],
        summary="Create remote entity",
    ),
)
@method_decorator(
    name="retrieve",
    decorator=extend_schema(
        tags=["remote-entities"],
        summary="Retrieve remote entity",
    ),
)
@method_decorator(
    name="update",
    decorator=extend_schema(
        tags=["remote-entities"],
        summary="Update remote entity details",
    ),
)
@method_decorator(
    name="destroy",
    decorator=extend_schema(
        tags=["remote-entities"],
        summary="Delete remote entity",
    ),
)
@extend_schema_view(partial_update=extend_schema(exclude=True))
@permission_classes([IsAuthenticated])
class RemoteEntityViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = RemoteEntity.objects.all()

    SERIALIZER_MAP: Final[dict[str, type[serializers.Serializer]]] = {
        "create": RemoteEntitySerializer,
        "list": RemoteEntitySerializer,
        "retrieve": RemoteEntitySerializer,
        "activate": RemoteEntityUpdateStatusSerializer,
        "update": RemoteEntitySerializer,
    }

    def get_serializer_class(self) -> type[serializers.Serializer]:
        return self.SERIALIZER_MAP[self.action]

    @extend_schema(summary="List all remote entities")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Change active status for remote entity")
    @action(methods=("PATCH",), detail=True)
    def activate(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
