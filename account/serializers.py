from rest_framework import serializers

from account.models import UserLanguageProfile, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile


class UserLanguageProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLanguageProfile
