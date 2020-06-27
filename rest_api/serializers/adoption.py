from rest_framework import serializers
from rest_api.models.adoption import AdoptionRequest

from rest_api.serializers.profile import ProfileEmailSerializer


class AdoptionRequestSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = AdoptionRequest
        fields = '__all__'


class AdoptionRequestColaboratorsSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    user = ProfileEmailSerializer(read_only=True, source="potencial_adopter")

    class Meta:
        """Map this serializer to a model and their fields."""
        model = AdoptionRequest
        fields = ('user',)