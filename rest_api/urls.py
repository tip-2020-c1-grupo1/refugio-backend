from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView, UserDetailsView, AnimalViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers, renderers

router = routers.DefaultRouter()
router.register(r'animals', AnimalViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    path('users/', UserView.as_view(), name="users"),
    path('users/(<int:pk>/',
        UserDetailsView.as_view(), name="user_details"),
    path('get-token/', obtain_auth_token),
]
