import random

from django.shortcuts import get_object_or_404
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets

from account.models import LearningLevels
from core.serializers import UserSerializer
from language.models import Language
from language.serializers import LanguageSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

    def list(self, request, *args, **kwargs):
        serialized_data = LanguageSerializer(self.get_queryset(), many=True)
        return Response({'success': True, 'results': serialized_data.data})

    @detail_route()
    def get_known_user(self, request, pk):
        language = get_object_or_404(self.get_queryset(), pk=pk)  # type: Language
        language_profiles = language.users.filter(
            learning__in=[LearningLevels.KNOW, LearningLevels.PROFICIENT]).exclude(
            user=request.user)
        total_such_profiles = language_profiles.count()
        random_val = random.randrange(0, total_such_profiles)
        language_profiles = language_profiles[random_val:random_val+1]
        if len(language_profiles) > 0:
            language_profile = language_profiles[0]
        else:
            return Response(None)
        return Response(UserSerializer(language_profile.user).data)
