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
