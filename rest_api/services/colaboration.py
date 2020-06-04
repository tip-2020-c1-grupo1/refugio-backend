from rest_api.models.colaboration import Colaboration
from rest_api.services.profile import ProfileService

class ColaborationRequestService(object):

    @staticmethod
    def create_with(email, colab_pk):
        profile = ProfileService.get_by_email(email)
        colab = Colaboration.objects.get(pk=colab_pk)
        colab.status_request = 'RESERVADO'
        colab.colaborator = profile
        return colab.save()
