from typing import Final

from django.utils.decorators import method_decorator
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import mixins, viewsets, serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from ..models import IdentityRole
from ..serializers import IdentityRoleSerializer


@method_decorator(
    name='create',
    decorator=extend_schema(
        tags=['roles'],
        summary='Create identity role',

    ),
)
@method_decorator(
    name='retrieve',
    decorator=extend_schema(
        tags=['roles'],
        summary='Retrieve identity role',

    ),
)
@method_decorator(
    name='destroy',
    decorator=extend_schema(
        tags=['roles'],
        summary='Delete identity role',

    ),
)
@permission_classes([IsAuthenticated])
class IdentityRoleViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    # mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = IdentityRole.objects.all()

    SERIALIZER_MAP: Final[dict[str, type[serializers.Serializer]]] = {
        'create': IdentityRoleSerializer,
        'list': IdentityRoleSerializer,
        'retrieve': IdentityRoleSerializer,
        # 'update': RecurringIssueUpdateSerializer,
        # 'partial_update': RecurringIssueUpdateSerializer,
    }

    def get_serializer_class(self) -> type[serializers.Serializer]:
        return self.SERIALIZER_MAP[self.action]

    # @extend_schema(
    #     summary="Update identity role",
    # )
    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)
    #
    # @extend_schema(
    #     summary="Update identity role",
    # )
    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="List all identity roles")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
