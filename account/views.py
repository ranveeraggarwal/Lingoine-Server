from rest_framework import viewsets

from account.models import UserProfile, UserLanguageProfile
from account.serializers import UserProfileSerializer, UserLanguageProfileSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserLanguageViewSet(viewsets.ModelViewSet):
    serializer_class = UserLanguageProfileSerializer
    queryset = UserLanguageProfile.objects.all()
