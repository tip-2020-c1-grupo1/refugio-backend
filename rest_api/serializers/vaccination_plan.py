from rest_framework import serializers
from rest_api.models.vaccination_plan import VaccinationPlan


class VaccinationPlanSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = VaccinationPlan
        fields = ('pk', 'description')