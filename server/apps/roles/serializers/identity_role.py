# write create / update / delete methods for IdentityRoleSerializer

from rest_framework import serializers

from ..models import IdentityRole


class IdentityRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRole
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        validated_data["updated_by"] = user
        return IdentityRole.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context["request"].user
        validated_data["updated_by"] = user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class RoleUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRole
        fields = ["is_active"]

    def update(self, instance, validated_data: dict):
        user = self.context["request"].user
        validated_data["updated_by"] = user
        instance.save()
        updated_role = super().update(instance, validated_data)
        # TODO:- state check for concurrent usage (model + migration update)
        # TODO:- archiving / deactivation logic for dependent entities

        return updated_role
