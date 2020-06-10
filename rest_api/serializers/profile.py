from rest_framework import serializers
from rest_api.models.animals import Animal
from rest_api.models.profile import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = '__all__'


class ProfileEmailSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True, source="user.email")
    first_name = serializers.CharField(read_only=True, source="user.first_name")
    last_name = serializers.CharField(read_only=True, source="user.last_name")

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    animals = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Animal.objects.all())
    username = serializers.CharField(read_only=True, source="user.username")
    first_name = serializers.CharField(read_only=True, source="user.first_name")
    last_name = serializers.CharField(read_only=True, source="user.last_name")
    email = serializers.CharField(read_only=True, source="user.email")

    class Meta:
        """Map this serializer to the default django user model."""
        model = Profile
        fields = ('google_id', 'phone', 'image_url', 'type_of_profile', 'username', 'first_name', 'last_name', 'email', 'animals')
        depth = 1