from rest_framework import serializers
from rest_api.models.timeline import Timeline


class TimelineSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Timeline
        fields = '__all__'