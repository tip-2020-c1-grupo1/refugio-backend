from rest_framework import serializers
from rest_api.models.refugio_event import RefugioEvent


class RefugioEventSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = RefugioEvent
        fields = '__all__'