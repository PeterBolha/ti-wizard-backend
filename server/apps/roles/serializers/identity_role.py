# write create / update / delete methods for IdentityRoleSerializer

from rest_framework import serializers
from ..models import IdentityRole


class IdentityRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRole
        fields = '__all__'


class RoleUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRole
        fields = ['is_active']

    def update(self, instance, validated_data: dict):
        updated_role = super().update(instance, validated_data)

        # TODO:- archiving / deactivation logic for dependent entities

        return updated_role

