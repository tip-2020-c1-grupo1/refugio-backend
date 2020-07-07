from rest_framework import serializers

from rest_api.models.adoption import AdoptionRequest
from rest_api.models.animals import Animal, ImageAnimal, AnimalSpecie
from rest_api.serializers.adoption import AdoptionRequestColaboratorsSerializer


class ImageSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    animal = serializers.ReadOnlyField(source='animal.name')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = ImageAnimal
        fields = ('id', 'image', 'animal')


class ImageSerializerSimple(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = ImageAnimal
        fields = ('id', 'image')


class AnimalSpecieSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = AnimalSpecie
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    images = ImageSerializerSimple(many=True, required=False)
    specie = serializers.CharField(read_only=True, source="species.name")
    requesters = serializers.SerializerMethodField()
    """
    requesters = AdoptionRequestColaboratorsSerializer(read_only=True,
                                                       many=True,
                                                       source="adoption_requests_for_animal")
    """
    def get_requesters(self, obj):
        adoption_requests = obj.adoption_requests_for_animal.exclude(
            status__in=['Adoptado', 'En revisión', 'Eliminado'])
        return AdoptionRequestColaboratorsSerializer(adoption_requests, many=True).data

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Animal
        fields = ('id', 'name', 'requesters', 'description', 'long_description', 'vaccination_plan', 'status_request', 'specie', 'race', 'gender', 'owner', 'images','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

