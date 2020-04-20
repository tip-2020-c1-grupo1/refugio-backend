from rest_framework import generics, permissions, viewsets
from .permissions import IsOwner
from .serializers import UserSerializer, AnimalSerializer
from .models import Animal
from django.contrib.auth.models import User


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    # queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Animal.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset