from rest_api.models.colaboration import Colaboration
from rest_api.services.profile import ProfileService

class ColaborationRequestService(object):

    @staticmethod
    def add_colaboration(email, colab_pk):
        profile = ProfileService.get_by_email(email)
        colab = Colaboration.objects.get(pk=colab_pk)
        colab.colaborators.add(profile)
        colab.save()
        colab.satisfied = colab.colaborators.count() == colab.required_colaborators
        if colab.satisfied:
            colab.status_request = 'Reservado'
        return colab.save()

    @staticmethod
    def remove_colaboration(email, pk):
        profile = ProfileService.get_by_email(email)
        colab = Colaboration.objects.get(pk=pk)
        colab.colaborators.remove(profile)
        colab.save()

        colab.satisfied = colab.colaborators.count() == colab.required_colaborators
        if not colab.satisfied:
            colab.status_request = 'Disponible'
        return colab.save()

    @staticmethod
    def is_satisfied(colab_pk):
        colab = Colaboration.objects.get(pk=colab_pk)
        return colab.satisfied