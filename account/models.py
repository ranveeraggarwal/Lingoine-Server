from django.contrib.auth.models import User
from django.db import models

from language.models import Language


class LearningLevels:
    KNOW = 1
    PROFICIENT = 2
    LEARNING = 3

    @classmethod
    def options(cls):
        return ((cls.KNOW, 'Beginner'), (cls.PROFICIENT, 'Intermediate'),
                (cls.LEARNING, 'Advanced'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    picture = models.URLField()
    location = models.CharField(max_length=64)
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class UserLanguageProfile(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    language = models.ForeignKey(Language)
    experience_rating = models.FloatField(default=0.0)
    proficiency_rating = models.FloatField(default=0.0)
    learning = models.IntegerField(default=LearningLevels.LEARNING, blank=True, null=True,
                                   choices=LearningLevels.options())
    is_expert = models.BooleanField(default=False)
    documents = models.BooleanField(default=False)  # TODO: Make this a file field
