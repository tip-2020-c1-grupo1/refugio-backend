from rest_framework import status, viewsets
from rest_api.models.complaint import Complaint
from rest_api.serializers.complaint import ComplaintSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_api.services.complaint import ComplaintService


class ComplaintViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = ComplaintSerializer

    def get_queryset(self):
        base_queryset = Complaint.objects.all()
        search = self.request.query_params.get('status_request', None)
        if search is not None:
            base_queryset = base_queryset.filter(status_request=search)
        return base_queryset

    @action(detail=False, methods=['post'])
    def make_complaint(self, request):
        data = request.data
        if 'email' not in data or 'description' not in data:
            content = {'Error': 'Falta ingresar usuario o descripción'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        ComplaintService.create_with(data['email'], data['description'])

        return Response({'Ok': 'Se creo su denuncia con exito'}, status=status.HTTP_200_OK)
