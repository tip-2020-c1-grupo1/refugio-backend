from rest_api.models.complaint import Complaint
from rest_api.services.profile import ProfileService


class ComplaintService(object):

    @staticmethod
    def create_with(email, description):
        profile = ProfileService.get_by_email(email)
        return Complaint.objects.create(complainer=profile, description=description)
