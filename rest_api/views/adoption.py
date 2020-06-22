from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_api.models.adoption import AdoptionRequest
from rest_api.serializers.adoption import AdoptionRequestSerializer
from rest_api.services.adoption import AdoptionRequestService


class AdoptionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """
    serializer_class = AdoptionRequestSerializer
    queryset = AdoptionRequest.objects.all()

    @action(detail=False, methods=['post'])
    def remove_adoption_for_user(self, request):
        data = request.data
        if 'email' not in data:
            content = {'Error': 'Falta ingresar usuario'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        if 'animal_pk' not in data:
            content = {'Error': 'Falta ingresar animal'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        AdoptionRequestService.remove_adoption_for_user(data['email'], data['animal_pk'])
        return Response({'Ok': 'Se borro su solicitud de adopción con exito'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def request_adoption(self, request):
        data = request.data
        if 'email' not in data or 'animal_pk' not in data:
            content = {'Error': 'Falta ingresar usuario o animal'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        _, was_created = AdoptionRequestService.create_with(data['email'], data['animal_pk'])

        if was_created:
            content = {
                'Error': 'Usted ya intento solicitar la adopción de este animal en el pasado, volveremos a contactarlo'}
            return Response(content, status=status.HTTP_412_PRECONDITION_FAILED)

        return Response({'Ok': 'Se creo la solicitud de adopción con exito'}, status=status.HTTP_200_OK)
