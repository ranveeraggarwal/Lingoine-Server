from django.contrib import admin
from .models import UserProfile, UserLanguageProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'picture', 'location', 'premium']


@admin.register(UserLanguageProfile)
class UserLanguageProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_profile', 'language', 'experience_rating', 'proficiency_rating', 'learning',
                    'is_expert', 'documents']
