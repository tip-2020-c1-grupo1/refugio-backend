from rest_framework import serializers
from rest_api.models.adoption import AdoptionRequest


class AdoptionRequestSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = AdoptionRequest
        fields = '__all__'