from rest_framework import generics, viewsets

from rest_api.models.adoption import AdoptionRequest
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.serializers.animals import AnimalSerializer, ImageSerializerSimple


class AnimalViewSetAll(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """
    serializer_class = AnimalSerializer
    pagination_class = None

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        filter_elem = self.request.query_params.get('filter', None)
        state_list = self.request.query_params.get('state', None)
        user_email = self.request.query_params.get('user', None)
        requester = self.request.query_params.get('requester', None)
        animals = Animal.objects.all()

        if filter_elem is not None and search is not None:

            filters = filter_elem.split('_')

            if 'name' in filters and 'race' not in filters and 'species' not in filters:
                animals = Animal.objects.search_only_name(search)

            elif 'race' in filters and 'name' not in filters and 'species' not in filters:
                animals = Animal.objects.search_only_race(search)

            elif 'species' in filters and 'race' not in filters and 'name' not in filters:
                animals = Animal.objects.search_only_species(search)

            elif 'name' in filters and 'race' in filters and 'species' not in filters:
                animals = Animal.objects.search_only_name_and_race(search)

            elif 'name' in filters and 'race' not in filters and 'species' in filters:
                animals = Animal.objects.search_only_name_and_species(search)

            elif 'race' in filters and 'name' not in filters and 'species' in filters:
                animals = Animal.objects.search_only_race_and_species(search)

        elif search is not None:
            animals = Animal.objects.search_only_name_race_and_species(search)

        if state_list is not None:
            state = state_list.split('_')
            animals = animals.filter(status_request__in=state)

        if user_email is not None:

            animals = animals.filter(owner__user__email=user_email)

        elif requester is not None:
            adoption_requests = AdoptionRequest.objects.filter(potencial_adopter__user__email=requester).exclude(
                status__in=['Adoptado', 'Eliminado'])
            animals = animals.filter(adoption_requests_for_animal__in=adoption_requests)

        return animals


class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        filter_elem = self.request.query_params.get('filter', None)
        state_list = self.request.query_params.get('state', None)
        user_email = self.request.query_params.get('user', None)
        requester = self.request.query_params.get('requester', None)
        animals = Animal.objects.all()

        if filter_elem is not None and search is not None:
            
            filters = filter_elem.split('_')

            if 'name' in filters and 'race' not in filters and 'species' not in filters:
                animals = Animal.objects.search_only_name(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' not in filters:
                animals = Animal.objects.search_only_race(search)
                
            elif 'species' in filters and 'race' not in filters and 'name' not in filters:
                animals = Animal.objects.search_only_species(search)
            
            elif 'name' in filters and 'race' in filters and 'species' not in filters:
                animals = Animal.objects.search_only_name_and_race(search)
                
            elif 'name' in filters and 'race' not in filters and 'species' in filters:
                animals = Animal.objects.search_only_name_and_species(search)
                
            elif 'race' in filters and 'name' not in filters and 'species' in filters:
                animals = Animal.objects.search_only_race_and_species(search)

        elif search is not None:
            animals = Animal.objects.search_only_name_race_and_species(search)

        if state_list is not None:
            state = state_list.split('_')
            animals = animals.filter(status_request__in=state)

        if user_email is not None:

            animals = animals.filter(owner__user__email=user_email)

        elif requester is not None:
            adoption_requests = AdoptionRequest.objects.filter(potencial_adopter__user__email=requester).exclude(status__in=['Adoptado', 'Eliminado'])
            animals = animals.filter(adoption_requests_for_animal__in=adoption_requests)

        return animals


class ImageAnimalViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = ImageAnimal.objects.all()
    serializer_class = ImageSerializerSimple
