# write create / update / delete methods for IdentityRoleSerializer

from rest_framework import serializers
from ..models import IdentityRole


class IdentityRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityRole
        fields = '__all__'
