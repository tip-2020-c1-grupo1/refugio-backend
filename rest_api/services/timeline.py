class TimelineService(object):

    @staticmethod
    def create_initial_timeline(animal):
        from rest_api.models.timeline import Timeline
        timeline = Timeline.objects.create(animal=animal)
        from rest_api.services.refugio_event import RefugioEventService
        RefugioEventService.create_initial_event(timeline, animal)

    @staticmethod
    def update_references(animal, reported_by):
        from rest_api.models.timeline import Timeline
        timeline = Timeline.objects.get(animal=animal)
        from rest_api.services.refugio_event import RefugioEventService
        RefugioEventService.create_initial_event(timeline, animal)