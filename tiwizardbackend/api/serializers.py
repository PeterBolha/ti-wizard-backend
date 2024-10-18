from rest_framework import serializers
from rest_framework.serializers import Serializer


# TODO - Check supported values of URL and URI in entityid and metadata_url (valdiate?)
class SamlSpSerializer(Serializer):
    _id = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    entityid = serializers.CharField(required=True)
    metadata_url = serializers.CharField(required=True)


class SamlIdpSerializer(Serializer):
    _id = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    entityid = serializers.CharField(required=True)
    metadata_url = serializers.CharField(required=True)


class OidcOp(Serializer):
    _id = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    discovery_url = serializers.CharField(required=True)


class OidcRp(Serializer):
    _id = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    client_id = serializers.CharField(required=False)
    client_secret = serializers.CharField(required=False)
    redirect_uri = serializers.CharField(required=False)
    dynamic_registration = serializers.BooleanField(required=False)
