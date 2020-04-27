from django.urls import path, include

from rest_api.views.animals import AnimalViewSet
from rest_api.views.profile import UserReadOnlyView, ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'animals', AnimalViewSet, basename='Animal')
router.register(r'profiles', ProfileViewSet, basename='User')
router.register(r'users', UserReadOnlyView, basename='Profile')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', obtain_auth_token),
]
