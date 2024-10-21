from rest_framework import mixins, viewsets
from drf_spectacular.utils import extend_schema

from ..models import ActiveFederation
from ..serializers import ActiveFederationSerializer


class FederationViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ActiveFederation.objects.all()
    serializer_class = ActiveFederationSerializer

    # TODO:- could be added later if needed: permission_classes, filterset_class (filterset_fields, ordering_fields)

    # TODO:- you can add examples for extensive description of the API
    @extend_schema(description="Create a new federation")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(description="Delete a federation")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(description="List all federations")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
