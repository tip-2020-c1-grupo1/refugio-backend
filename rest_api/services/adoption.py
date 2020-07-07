from rest_api.services.animal import AnimalService
from rest_api.services.profile import ProfileService
from rest_api.models.adoption import AdoptionRequest
from rest_api.services.refugio_event import RefugioEventService

AVAILABLE = 'Disponible'
REQUESTED = 'Solicitado'
WAIT_LIST = 'En espera'
ACCEPTED = 'Aceptado'
REJECTED = 'Rechazado'
ON_HOLD = 'En revisión'
ADOPTED = 'Adoptado',
REMOVED = 'Eliminado'


class AdoptionRequestService(object):

    @staticmethod
    def create_with(email, animal_pk):
        profile = ProfileService.get_by_email(email)
        animal = AnimalService.get_by_id(animal_pk)
        adoption_request_list = AdoptionRequest.objects.filter(
            status=REQUESTED,
            potencial_adopter=profile,
            animal=animal
        )
        if adoption_request_list.exists():
            return adoption_request_list.first(), True
        adoption_request = AdoptionRequest.objects.create(
                status=REQUESTED, potencial_adopter=profile, animal=animal)
        RefugioEventService.create_adoption_request_event(profile, animal)
        return adoption_request, False

    @staticmethod
    def remove_adoption_for_user(email, pk):
        adoption_request = AdoptionRequest.objects.filter(animal_id=pk).filter(potencial_adopter__user__email=email).exclude(
            status__in=['Adoptado', 'En revisión', 'Eliminado']).first()
        adoption_request.status = REMOVED
        adoption_request.save()
        RefugioEventService.modify_adoption_request_event(adoption_request, email)
