from django.db import models

# Create your models here.
class DataEntry(models.Model):
    user =   models.TextField(blank=False, default=' ')
    model =  models.TextField(blank=False, default=' ')
    prompt = models.TextField(blank=False, default=' ')
    result = models.TextField(blank=False, default=' ')