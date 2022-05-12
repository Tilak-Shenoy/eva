from django.db import models

# Create your models here.
class Voices(models.Model):
    language = models.CharField(max_length=100, blank=False, default='')
    country = models.CharField(max_length=50, blank=False, default='')
    locale = models.CharField(max_length=5, blank=False, default='en-US')
    gender = models.CharField(max_length=6, blank=False, default='Female')
    voice_name = models.CharField(max_length=50, blank=False, default='')
