# server/apps/federations/serializers.py
from rest_framework import serializers

from server.apps.federations.models import ActiveFederation


class ActiveFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveFederation
        fields = ['id', 'federation_id', 'is_active']