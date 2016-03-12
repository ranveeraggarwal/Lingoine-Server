from rest_framework import serializers

from account.models import UserLanguageProfile, UserProfile
from language.models import Language


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile


class UserLanguageProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLanguageProfile


class LanguageListSerializer(serializers.Serializer):
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)


class LanguageLevelSerializer(serializers.Serializer):
    pass


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
