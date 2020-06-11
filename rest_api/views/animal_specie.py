from rest_framework import viewsets

from rest_api.models.animals import AnimalSpecie
from rest_api.serializers.animals import AnimalSpecieSerializer


class AnimalSpecieViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = AnimalSpecieSerializer
    queryset = AnimalSpecie.objects.all()

