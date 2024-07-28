from django.db import models


# Create your models here.
class Location(models.Model):

    name = models.CharField(max_length=250)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return self.name