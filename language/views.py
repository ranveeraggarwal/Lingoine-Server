from rest_framework.response import Response
from rest_framework import viewsets

from language.models import Language
from language.serializers import LanguageSerializer


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

    def list(self, request, *args, **kwargs):
        serialized_data = LanguageSerializer(self.get_queryset(), many=True)
        return Response({'success': True, 'results': serialized_data.data})
