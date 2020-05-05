from rest_api.services.animal import AnimalService
from rest_api.services.profile import ProfileService
from rest_api.models.adoption import AdoptionRequest
from rest_api.services.refugio_event import RefugioEventService

STARTED = 'STA'


class AdoptionRequestService(object):

    @staticmethod
    def create_with(email, animal_pk):
        profile = ProfileService.get_by_email(email)
        animal = AnimalService.get_by_id(animal_pk)
        adoption_request, was_created = AdoptionRequest.objects.get_or_create(
            status=STARTED, potencial_adopter=profile, animal=animal)
        if not was_created:
            RefugioEventService.create_adoption_request_event(profile, animal)
        return adoption_request
