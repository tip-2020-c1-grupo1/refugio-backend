from django.contrib.auth.models import User
from django.test import TestCase
from rest_api.services.profile import ProfileService


class AnimalTestCase(TestCase):
    def setUp(self):
        self.some_email = 'custom@email.com'
        self.google_id = 'some_google_id'
        self.image_url = 'some_image_url'

    def test_user_created_with_profile_given_data(self):
        data = {
            'email': 'custom@email.com',
            'givenName': 'some_name',
            'familyName': 'some_surname',
            'name': 'some_username',
            'googleId': 'some_google_id',
            'imageUrl': 'some_image_url'
        }
        profile = ProfileService.prepare_profile(data)

        self.assertEqual(profile.image_url, 'some_image_url')
        self.assertEqual(profile.user.first_name, 'some_name')
        self.assertFalse(profile.user.is_superuser)
        self.assertFalse(profile.user.is_staff)

    def test_user_already_created_with_profile_given_data(self):
        user = User.objects.create_user('pepe',
                                             is_staff=False,
                                             is_superuser=False,
                                             password='pepe',
                                             email='pepe@user.com')
        data = {
            'email': 'pepe@user.com',
            'givenName': 'some_name',
            'familyName': 'some_surname',
            'name': 'pepe',
            'googleId': 'some_google_id',
            'imageUrl': 'some_image_url'
        }
        profile = ProfileService.prepare_profile(data)

        self.assertEqual(profile.image_url, 'some_image_url')
        self.assertEqual(profile.user.username, 'pepe')
        self.assertTrue(User.objects.filter(email=user.email).count() == 1)
