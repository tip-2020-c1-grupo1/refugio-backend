from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from rest_api.views.adoption import AdoptionViewSet
from rest_api.views.animal_specie import AnimalSpecieViewSet
from rest_api.views.animals import AnimalViewSet, AnimalViewSetAll
from rest_api.views.colaboration import ColaborationViewSet
from rest_api.views.complaint import ComplaintViewSet
from rest_api.views.mercadopago import get_preference_id
from rest_api.views.profile import UserReadOnlyView, ProfileViewSet
from rest_api.views.refugio_event import RefugioEventViewSet
from rest_api.views.timeline import TimelineViewSet

router = routers.DefaultRouter()
router.register(r'animals_all', AnimalViewSetAll, basename='AnimalAll')
router.register(r'animals', AnimalViewSet, basename='Animal')
router.register(r'profiles', ProfileViewSet, basename='User')
router.register(r'users', UserReadOnlyView, basename='Profile')
router.register(r'timelines', TimelineViewSet, basename='Timeline')
router.register(r'events', RefugioEventViewSet, basename='RefugioEvent')
router.register(r'adoption', AdoptionViewSet, basename='Adoption')
router.register(r'colaboration', ColaborationViewSet, basename='Colaboration')
router.register(r'complaint', ComplaintViewSet, basename='Complaint')
router.register(r'animal_specie', AnimalSpecieViewSet, basename='AnimalSpecie')

urlpatterns = [
    path('preference_id', get_preference_id),
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
