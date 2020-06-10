from rest_framework import serializers
from rest_api.models.complaint import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Complaint
        fields = '__all__'