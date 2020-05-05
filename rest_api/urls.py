from django.urls import path, include

from rest_api.views.refugio_event import RefugioEventViewSet
from rest_api.views.timeline import TimelineViewSet
from rest_api.views.animals import AnimalViewSet
from rest_api.views.profile import UserReadOnlyView, ProfileViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'animals', AnimalViewSet, basename='Animal')
router.register(r'profiles', ProfileViewSet, basename='User')
router.register(r'users', UserReadOnlyView, basename='Profile')
router.register(r'timelines', TimelineViewSet, basename='Timeline')
router.register(r'events', RefugioEventViewSet, basename='RefugioEvent')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-token/', obtain_auth_token),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
