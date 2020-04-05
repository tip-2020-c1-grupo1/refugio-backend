from rest_framework import generics, permissions, viewsets
from .permissions import IsOwner
from .serializers import UserSerializer, AnimalSerializer
from .models import Animal
from django.contrib.auth.models import User


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer