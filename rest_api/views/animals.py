from rest_framework import generics, viewsets
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.serializers.animals import AnimalSerializer, ImageSerializerSimple


class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        filter_elem = self.request.query_params.get('filter', None)
        state_list = self.request.query_params.get('state', None)
        animals = Animal.objects.all()

        if filter_elem is not None and state_list is not None:
            
            filters = filter_elem.split('_')
            state = state_list.split('_')

            if 'name' in filters and 'race' not in filters and 'species' not in filters and search is not None:
                animals =  Animal.objects.search_only_name(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' not in filters and search is not None:
                animals = Animal.objects.search_only_race(search)
                
            elif 'species' in filters and 'race' not in filters and 'name' not in filters and search is not None:
                animals = Animal.objects.search_only_species(search)
            
            elif 'name' in filters and 'race' in filters and 'species' not in filters and search is not None:
                animals = Animal.objects.search_only_name_and_race(search)
                
            elif 'name' in filters and 'race' not in filters and 'species' in filters and search is not None:
                animals = Animal.objects.search_only_name_and_species(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' in filters and search is not None:
                animals = Animal.objects.search_only_race_and_species(search)
                
            elif 'species' in filters and 'race' in filters and 'name' in filters and search is not None:
                animals = Animal.objects.search_only_name_race_and_species(search)
            return animals.filter(status_request__in=state)
        return animals


class ImageAnimalViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = ImageAnimal.objects.all()
    serializer_class = ImageSerializerSimple
