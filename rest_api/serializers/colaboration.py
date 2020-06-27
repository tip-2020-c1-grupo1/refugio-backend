from rest_framework import serializers
from rest_api.models.colaboration import Colaboration, ColaborationColaborators


class ColaborationSingleColaboratorSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    email = serializers.CharField(read_only=True, source="colaborator.user.email")
    first_name = serializers.CharField(read_only=True, source="colaborator.user.first_name")
    last_name = serializers.CharField(read_only=True, source="colaborator.user.last_name")

    class Meta:
        model = ColaborationColaborators
        fields = ('email', 'first_name', 'last_name')
        deep = 1


class ColaborationSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    colaborators = ColaborationSingleColaboratorSerializer(many=True, read_only=True, source="colaboration_colab")

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Colaboration
        fields = ('id', 'name', 'short_description', 'description', 'status_request',
              'satisfied', 'required_colaborators', 'colaborators')
        deep = 1