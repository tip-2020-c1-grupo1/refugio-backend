from django.contrib.auth.models import User
from rest_api.models.profile import Profile


REFUGIO = 'REF'
ADMIN = 'ADM'
ADOPTER = 'ADO'
TYPES_OF_PROFILE_CHOICES = [
    (ADOPTER, 'Adoptante'),
    (REFUGIO, 'Refugio'),
    (ADMIN, 'Admin'),
]


class ProfileService(object):

    @staticmethod
    def create_profile(google_id, image_url, user, type_of_profile=ADOPTER, phone=''):
        return Profile.objects.create(image_url=image_url,
                                      google_id=google_id,
                                      user=user,
                                      type_of_profile=type_of_profile,
                                      phone=phone)

    @staticmethod
    def get_by_email(email):
        return Profile.objects.get_by_email(email)

    @staticmethod
    def get_profile(data):
        user = User.objects.filter(email=data['email']).first()
        if user is None:
            from django.contrib.auth.hashers import make_password

            user = User.objects.create(email=data['email'],
                                       first_name=data['givenName'],
                                       last_name=data['familyName'],
                                       username=data['name'],
                                       is_staff=False,
                                       is_superuser=False,
                                       password=make_password(data['name']))
        profile = Profile.objects.filter(user__email=data['email']).first()
        image_url = data['imageUrl']
        google_id = data['googleId']
        if profile is None:
            phone = ''
            if 'phone' in data:
                phone = data['phone']
            profile = ProfileService.create_profile(google_id, image_url, user, phone)
        if profile.image_url == '' and image_url != '':
            if 'phone' in data:
                profile.phone = data['phone']
            profile.image_url = image_url
            profile.google_id = google_id
            profile.save()
        return profile