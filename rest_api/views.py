from rest_framework import generics, permissions, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import UserSerializer, AnimalSerializer
from .models import Animal
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from .models import Animal, ImageAnimal
from .serializers import UserSerializer, AnimalSerializer, ImageSerializerSimple
from django.core.cache import cache

REDIRECTS_KEY = "animals.all"

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @method_decorator(cache_page(None))
    def list(self, request, format=None):
        data = cache.get(REDIRECTS_KEY)
        if not data:
            data = Animal.objects.all()
            cache.set(REDIRECTS_KEY, data)
            print('Caching objects now')
        else:
            print('With Cached objects')
        name = self.request.query_params.get('name', None)
        if name is not None:
            data = data.filter(name__icontains=name)
        serializer = AnimalSerializer(data, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        data = cache.get(REDIRECTS_KEY)
        if not data:
            data = Animal.objects.all()
            cache.set(REDIRECTS_KEY, data)
        animal = get_object_or_404(data, pk=pk)
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)
    # queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class ImageAnimalViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = ImageAnimal.objects.all()
    serializer_class = ImageSerializerSimple
