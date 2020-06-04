from rest_framework import serializers
from rest_api.models.colaboration import Colaboration


class ColaborationSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Colaboration
        fields = '__all__'