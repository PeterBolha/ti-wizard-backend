from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import mixins, viewsets

from ..models import ActiveFederation
from ..serializers import ActiveFederationSerializer


class FederationViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = ActiveFederation.objects.all()
    serializer_class = ActiveFederationSerializer

    # TODO:- could be added later if needed: permission_classes, filterset_class
    #  (filterset_fields, ordering_fields)

    # TODO:- you can add examples for extensive description of the API
    @extend_schema(
        summary="Activate federation",
        examples=[
            OpenApiExample(
                "Payload example",
                value={"url": "https://federation.example.com"},
                request_only=True,
                response_only=False,
            ),
            OpenApiExample(
                "Response example",
                value={"id": 1, "url": "https://federation.example.com"},
                request_only=False,
                response_only=True,
            ),
        ],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Deactivate federation")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(summary="List all federations")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
