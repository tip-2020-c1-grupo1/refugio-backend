from rest_api.models.animals import Animal
from rest_api.models.refugio_event import RefugioEvent

AVAILABLE = 'AVA'
STARTED = 'STA'
WAIT_LIST = 'WAL'
ACCEPTED = 'ACC'
REJECTED = 'REJ'
ON_HOLD = 'ONH'
ADOPTED = 'ADO'

TYPES_OF_REQUEST_CHOICES = {
    AVAILABLE: 'Disponible',
    STARTED: 'Comenzo',
    WAIT_LIST: 'En espera',
    ACCEPTED: 'Aceptado',
    REJECTED: 'Rechazado',
    ON_HOLD: 'En revisión',
    ADOPTED: 'Adoptado',
}


class RefugioEventService(object):

    @staticmethod
    def create_initial_event(timeline, animal=None):
        """
        Refugio Events cannot be deleted
        """
        if animal is None:
            animal = timeline.animal
        metadata = animal.name + ' - PK: ' + str(animal.pk) + ' ha sido ingresado al sistema'
        return RefugioEvent.objects.create(timeline=timeline,
                                           metadata=metadata,
                                           description=metadata)

    @staticmethod
    def create_adoption_request_event(adopter, animal):
        """
        Refugio Events cannot be deleted
        """
        from rest_api.models.timeline import Timeline
        timeline = Timeline.objects.get(animal=animal)
        animal = timeline.animal
        email = adopter.user.email
        metadata = str({'animal': str(animal.pk), 'adopter_email': email})
        description = animal.name + ' - PK: ' + str(animal.pk) + ' quiere ser adoptado por el usuario cuyo mail es ' + email

        return RefugioEvent.objects.create(timeline=timeline,
                                           description=description,
                                           metadata=metadata)

    @staticmethod
    def modify_adoption_request_event(adoption_request,requester_email):
        """
        Refugio Events cannot be deleted
        """
        animal = adoption_request.animal
        from rest_api.models.timeline import Timeline
        from rest_api.models.profile import Profile
        profile = Profile.objects.get(user__email=requester_email)
        timeline = Timeline.objects.get(animal=animal)
        animal = timeline.animal
        animal_pk = str(animal.pk)
        email = adoption_request.potencial_adopter.user.email
        status = TYPES_OF_REQUEST_CHOICES[adoption_request.status]
        metadata = str({'animal': animal_pk, 'adopter_email': email,
                        'requested_by': requester_email,
                        'status': status})

        description = animal.name + ' - PK: ' + animal_pk + ' cuya solicitud fue iniciada por el usuario cuyo mail es: '
        description += email + ' paso a ' + status + ' por ' + requester_email

        animal.status_request = status
        animal.save()

        return RefugioEvent.objects.create(timeline=timeline,
                                           description=description,
                                           reported_by=profile,
                                           metadata=metadata)