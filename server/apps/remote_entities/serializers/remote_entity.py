# write create / update / delete methods for RemoteEntitySerializer

from rest_framework import serializers

from ..models.remote_entity import RemoteEntity


class RemoteEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteEntity
        fields = "__all__"

    # Propagate custom validation errors to the user in a friendly form
    def validate(self, data):
        instance = RemoteEntity(**data)
        instance.clean()
        return data

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = user
        validated_data["updated_by"] = user
        return RemoteEntity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = self.context["request"].user
        validated_data["updated_by"] = user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class RemoteEntityUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteEntity
        fields = ["is_active"]

    def update(self, instance, validated_data: dict):
        user = self.context["request"].user
        validated_data["updated_by"] = user
        instance.save()
        updated_remote_entity = super().update(instance, validated_data)
        # TODO:- state check for concurrent usage (model + migration update)
        # TODO:- archiving / deactivation logic for dependent entities

        return updated_remote_entity
