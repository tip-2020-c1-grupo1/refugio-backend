from rest_api.models.animals import Animal


class AnimalService(object):

    @staticmethod
    def get_by_id(pk):
        return Animal.objects.get(pk=pk)
