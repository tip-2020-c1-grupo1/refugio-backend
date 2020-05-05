from rest_framework import viewsets

from rest_api.models.refugio_event import RefugioEvent
from rest_api.serializers.refugio_event import RefugioEventSerializer


class RefugioEventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = RefugioEventSerializer
    queryset = RefugioEvent.objects.all()
