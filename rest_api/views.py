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
        search = self.request.query_params.get('search', None)
        filter_elem = self.request.query_params.get('filter', None)
        if filter_elem is not None: 
            
            filters = filter_elem.split('_')
            
            if 'name' in filters and 'race' not in filters and 'species' not in filters and search is not None:
                return Animal.objects.search_only_name(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' not in filters and search is not None:
                return Animal.objects.search_only_race(search)
                
            elif 'species' in filters and 'race' not in filters and 'name' not in filters and search is not None:
                return Animal.objects.search_only_species(search)
            
            elif 'name' in filters and 'race' in filters and 'species' not in filters and search is not None:
                return Animal.objects.search_only_name_and_race(search)
                
            elif 'name' in filters and 'race' not in filters and 'species' in filters and search is not None:
                return Animal.objects.search_only_name_and_species(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' in filters and search is not None:
                return Animal.objects.search_only_race_and_species(search)
                
            elif 'species' in filters and 'race' in filters and 'name' in filters and search is not None:
                return Animal.objects.search_only_name_race_and_species(search)
            
        return Animal.objects.all()

class ImageAnimalViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = ImageAnimal.objects.all()
    serializer_class = ImageSerializerSimple
