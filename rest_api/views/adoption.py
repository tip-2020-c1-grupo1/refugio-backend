from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_api.services.adoption import AdoptionRequestService


@api_view(['POST'])
def request_adoption(request):
    data = request.data
    if 'email' not in data or 'animal_pk' not in data:
        content = {'Error': 'Falta ingresar usuario o animal'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    _, was_created = AdoptionRequestService.create_with(data['email'], data['animal_pk'])

    if was_created:
        content = {
            'Error': 'Usted ya intento solicitar la adopción de este animal en el pasado, volveremos a contactarlo'}
        return Response(content, status=status.HTTP_412_PRECONDITION_FAILED)
    return Response({'Ok': 'Se creo la solicitud de adopción con exito'})
