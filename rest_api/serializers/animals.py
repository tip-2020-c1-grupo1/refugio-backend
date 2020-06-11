from rest_framework import serializers
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.serializers.vaccination_plan import VaccinationPlanSerializer


class ImageSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    animal = serializers.ReadOnlyField(source='animal.name')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = ImageAnimal
        fields = ('id','image' ,'animal')


class ImageSerializerSimple(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = ImageAnimal
        fields = ('id', 'image')


class AnimalSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""
    # source='vaccination_plan_animals', 
    vaccination_plan_animals = VaccinationPlanSerializer(read_only=True)
    images = ImageSerializerSimple(many=True, required=False)

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Animal
        fields = ('id', 'name', 'description', 'vaccination_plan_animals', 'status_request', 'species', 'race', 'gender', 'owner', 'images','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

