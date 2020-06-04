from rest_framework import status, viewsets
from rest_api.models.colaboration import Colaboration
from rest_api.serializers.colaboration import ColaborationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_api.services.colaboration import ColaborationRequestService


class ColaborationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = ColaborationSerializer

    def get_queryset(self):
        base_queryset = Colaboration.objects.all()
        search = self.request.query_params.get('status_request', None)
        if search is not None:
            base_queryset = base_queryset.filter(status_request=search)
        return base_queryset

    @action(detail=False, methods=['post'])
    def request_colab(self, request):
        data = request.data
        if 'email' not in data or 'colab_pk' not in data:
            content = {'Error': 'Falta ingresar usuario o animal'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        ColaborationRequestService.create_with(data['email'], data['colab_pk'])

        return Response({'Ok': 'Se asigno su calificación con exito'}, status=status.HTTP_200_OK)
