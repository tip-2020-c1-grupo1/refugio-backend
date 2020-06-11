from rest_framework import viewsets

from rest_api.models.vaccination_plan import VaccinationPlan
from rest_api.serializers.vaccination_plan import VaccinationPlanSerializer


class VaccinationPlanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving animals.
    """ 
    serializer_class = VaccinationPlanSerializer
    queryset = VaccinationPlan.objects.all()

