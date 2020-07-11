from rest_api.models.colaboration import Colaboration, ColaborationColaborators
from rest_api.services.profile import ProfileService


class ColaborationRequestService(object):

    @staticmethod
    def add_colaboration(email, colab_pk):
        profile = ProfileService.get_by_email(email)
        colab = Colaboration.objects.get(pk=colab_pk)
        ColaborationColaborators.objects.create(colaborator=profile, colaboration=colab)

    @staticmethod
    def remove_colaboration(email, pk):
        profile = ProfileService.get_by_email(email)
        colab = Colaboration.objects.get(pk=pk)
        to_remove = ColaborationColaborators.objects.get(colaborator=profile, colaboration=colab)
        to_remove.delete()
        ColaborationRequestService.change_status_colaboration(colab)

    @staticmethod
    def change_status_colaboration(colaboration):
        others = ColaborationColaborators.objects.filter(colaboration=colaboration).filter(
            status_request=Colaboration.CONFIRMED)
        satisfied = colaboration.required_colaborators == others.count()
        if satisfied:
            colaboration.satisfied = satisfied
            colaboration.status_request = Colaboration.CONFIRMED
        else:
            colaboration.satisfied = satisfied
            colaboration.status_request = Colaboration.AVAILABLE
        colaboration.save()

    @staticmethod
    def is_satisfied(colab_pk):
        colab = Colaboration.objects.get(pk=colab_pk)
        return colab.satisfied