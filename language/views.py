from rest_framework import viewsets

from language.models import Language
from language.serializers import LanguageSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
