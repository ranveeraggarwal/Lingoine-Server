import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from language.models import Language


class LearningLevels:
    KNOW = 1
    PROFICIENT = 2
    LEARNING = 3

    @classmethod
    def options(cls):
        return ((cls.KNOW, 'Know'), (cls.PROFICIENT, 'Proficient'),
                (cls.LEARNING, 'Learning'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    picture = models.URLField()
    location = models.CharField(max_length=64)
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class UserLanguageProfile(models.Model):
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language, related_name='users')
    experience_rating = models.FloatField(default=0.0)
    proficiency_rating = models.FloatField(default=0.0)
    learning = models.IntegerField(default=LearningLevels.LEARNING, blank=True, null=True,
                                   choices=LearningLevels.options())
    is_expert = models.BooleanField(default=False)
    documents = models.BooleanField(default=False)  # TODO: Make this a file field


class UserToken(models.Model):
    user = models.ForeignKey(User)
    token = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(default=timezone.now)
    has_expired = models.BooleanField(default=False)

    def is_active(self):
        if self.has_expired:
            return False
        curr_date = timezone.now()
        diff = abs((curr_date - self.last_accessed).days)
        # 1 month expiration date
        if diff > 30:
            self.has_expired = True
            self.save()
            return False
        else:
            self.last_accessed = curr_date
            self.save()
            return True
