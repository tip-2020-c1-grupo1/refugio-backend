from rest_framework import status, viewsets
from rest_api.models.colaboration import Colaboration, ColaborationColaborators
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
        user_email = self.request.query_params.get('user_email', None)

        if user_email is not None:
            from rest_api.models.profile import Profile
            profile = Profile.objects.get(user__email=user_email)
            colaborations_colaborators = ColaborationColaborators.objects.filter(colaborator=profile)
            base_queryset = base_queryset.filter(colaboration_colab__in=colaborations_colaborators)
        if search is not None:
            base_queryset = base_queryset.filter(status_request=search)
        return base_queryset

    @action(detail=True, methods=['post'])
    def remove_colab_for_user(self, request, pk=None):
        data = request.data
        if 'email' not in data:
            content = {'Error': 'Falta ingresar usuario'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        ColaborationRequestService.remove_colaboration(data['email'], pk)
        return Response({'Ok': 'Se borro su colaboración con exito'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def request_colab(self, request):
        data = request.data
        if 'email' not in data or 'colab_pk' not in data:
            content = {'Error': 'Falta ingresar usuario o colaboración'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        if ColaborationRequestService.is_satisfied(data['colab_pk']):
            content = {'Error': 'No se pueden agregar más colaboradores'}
            return Response(content, status=status.HTTP_412_PRECONDITION_FAILED)
        ColaborationRequestService.add_colaboration(data['email'], data['colab_pk'])

        return Response({'Ok': 'Se asigno su colaboración con exito'}, status=status.HTTP_200_OK)
