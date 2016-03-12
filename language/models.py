from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=64)
