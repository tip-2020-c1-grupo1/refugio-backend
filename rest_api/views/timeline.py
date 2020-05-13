from rest_api.serializers.timeline import TimelineSerializer

from rest_api.models.timeline import Timeline
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.serializers.json import DjangoJSONEncoder

from django.core.serializers import serialize
import json

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        #if isinstance(obj, Timeline):
        #    return str(obj)
        return super().default(obj)


class TimelineViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = TimelineSerializer
    queryset = Timeline.objects.all()

    @action(detail=True, methods=['get'])
    def by_animal(self, request, pk=None):
        data = request.data
        if pk is None:
            content = {'Error': 'Falta ingresar usuario o animal'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        from rest_api.models.refugio_event import RefugioEvent
        data = RefugioEvent.objects.filter(timeline__animal=pk).order_by('date_created')

        data = serialize('json', data, cls=LazyEncoder)
        data = json.loads(data)
        data = [elem['fields'] for elem in data]
        return Response(data, status=status.HTTP_200_OK)
