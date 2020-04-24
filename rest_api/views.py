from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import UserSerializer, AnimalSerializer
from .models import Animal
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .models import Animal, ImageAnimal
from .serializers import UserSerializer, AnimalSerializer, ImageSerializerSimple

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
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        queryset = Animal.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class ImageAnimalViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = ImageAnimal.objects.all()
    serializer_class = ImageSerializerSimple
