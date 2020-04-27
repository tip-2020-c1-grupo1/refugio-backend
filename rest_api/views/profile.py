from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_api.models.profile import Profile
from rest_api.serializers.profile import UserSerializer, ProfileSerializer
from rest_api.services.profile import ProfileService


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @action(detail=False, methods=['post'])
    def get_or_create_profile(self, request):
        data = request.data
        print(data)
        if 'email' not in data:
            content = {'Error': 'Please send email'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if 'googleId' not in data:
            content = {'Error': 'Please send googleId'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        profile = ProfileService.get_profile(data)

        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class UserReadOnlyView(viewsets.ReadOnlyModelViewSet):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

