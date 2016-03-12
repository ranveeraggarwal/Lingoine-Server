from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from account.models import UserProfile, UserLanguageProfile, UserToken
from account.serializers import UserProfileSerializer, UserLanguageProfileSerializer, LanguageListSerializer, \
    LanguageLevelSerializer, LoginSerializer
from core.mixins import SerializerClassRequestContextMixin
from language.serializers import LanguageSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserLanguageViewSet(viewsets.ModelViewSet, SerializerClassRequestContextMixin):
    serializer_class = UserLanguageProfileSerializer
    queryset = UserLanguageProfile.objects.all()
    permission_classes = [IsAuthenticated]

    @list_route(methods=['POST'])
    def set_know_languages(self, request):
        """
        Sets known languages for current user.
        ---
        request_serializer: LanguageListSerializer
        """
        serialized_data = LanguageListSerializer(data=request.data)
        if serialized_data.is_valid():
            languages = serialized_data.validated_data['languages']
            for language in languages:
                user_language = UserLanguageProfile.objects.create(
                    user=request.user,
                    language=language,
                    learning=1,
                )
                user_language.save()
            return Response({'success': True})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)

    @list_route(methods=['POST'])
    def set_proficient_languages(self, request):
        """
        Sets proficient languages for current user.
        ---
        request_serializer: LanguageListSerializer
        """
        serialized_data = LanguageListSerializer(data=request.data)
        if serialized_data.is_valid():
            languages = serialized_data.validated_data['languages']
            for language in languages:
                user_language = UserLanguageProfile.objects.create(
                    user=request.user,
                    language=language,
                    learning=2,
                )
                user_language.save()
            return Response({'success': True})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)

    @list_route(methods=['POST'])
    def set_learning_languages(self, request):
        """
        Sets learning languages for current user.
        ---
        request_serializer: LanguageListSerializer
        """
        serialized_data = LanguageListSerializer(data=request.data)
        if serialized_data.is_valid():
            languages = serialized_data.validated_data['languages']
            for language in languages:
                user_language = UserLanguageProfile.objects.create(
                    user=request.user,
                    language=language,
                    learning=3,
                )
                user_language.save()
            return Response({'success': True})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)

    @list_route()
    def get_know_languages(self, request):
        """
        Gets languages of type know for the current user.
        """
        serialized_data = LanguageLevelSerializer(data=request.data)
        if serialized_data.is_valid():
            data = self.get_queryset().filter(user=request.user, learning=1)
            user_languages = self.get_context_serializer_class(LanguageSerializer, data, many=True)
            return Response({'results': user_languages.data})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)

    @list_route()
    def get_proficient_languages(self, request):
        """
        Gets languages of type proficient for the current user.
        """
        serialized_data = LanguageLevelSerializer(data=request.data)
        if serialized_data.is_valid():
            data = self.get_queryset().filter(user=request.user, learning=2)
            user_languages = self.get_context_serializer_class(LanguageSerializer, data, many=True)
            return Response({'results': user_languages.data})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)

    @list_route()
    def get_learning_languages(self, request):
        """
        Gets languages of type learning for the current user.
        """
        serialized_data = LanguageLevelSerializer(data=request.data)
        if serialized_data.is_valid():
            data = self.get_queryset().filter(user=request.user, learning=3)
            user_languages = self.get_context_serializer_class(LanguageSerializer, data, many=True)
            return Response({'results': user_languages.data})
        else:
            return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)


class AccountViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    @list_route(methods=['POST'])
    def login(self, request):
        """
        Logs in the user.
        ---
        request_serializer: LoginSerializer
        """
        serialized_data = LoginSerializer(data=request.data)
        if serialized_data.is_valid():
            username = serialized_data.validated_data['username']

            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_unusable_password()
                UserProfile.objects.create(user=user)

            user.first_name = ""
            user.last_name = ""
            user.profile.picture = ""
            user.email = ""

            user.save()
            user.profile.save()

            user_token = UserToken.objects.create(user=user)
            return Response(
                    {
                        'success': True,
                        'token': user_token.token.hex,
                        'uid': User.objects.get(email=user.email).pk,
                    }
            )

        return Response(serialized_data.errors, status=HTTP_400_BAD_REQUEST)