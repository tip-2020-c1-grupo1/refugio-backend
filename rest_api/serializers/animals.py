from rest_framework import serializers
from rest_api.models.animals import Animal, ImageAnimal, AnimalSpecie


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

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Animal
        fields = ('id', 'name', 'description', 'vaccination_plan', 'status_request', 'specie', 'race', 'gender', 'owner', 'images','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

