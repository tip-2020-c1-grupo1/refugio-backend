from rest_framework import serializers
from rest_api.models.colaboration import Colaboration
from rest_api.serializers.profile import ProfileEmailSerializer


class ColaborationSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    colaborators = ProfileEmailSerializer(many=True, read_only=True)

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Colaboration
        fields = '__all__'
        """
        ('requesters', 'pk', 'name', 'short_description', 'description', 'status_request',
              'satisfied', 'required_colaborators' )
        """
        deep = 1