# server/apps/federations/serializers.py
from apps.federations.models import ActiveFederation
from rest_framework import serializers


class ActiveFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveFederation
        fields = ["id", "federation_id", "is_active"]
