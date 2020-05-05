from rest_framework import viewsets
from rest_api.serializers.timeline import TimelineSerializer

from rest_api.models.timeline import Timeline


class TimelineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = TimelineSerializer
    queryset = Timeline.objects.all()
