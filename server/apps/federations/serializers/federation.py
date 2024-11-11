# server/apps/federations/serializers.py
from rest_framework import serializers

from apps.federations.models import ActiveFederation


class ActiveFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveFederation
        fields = ["id", "url"]
