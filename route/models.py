from django.db import models
from location.models import Location


# Create your models here.
class Route(models.Model):
    class Level(models.TextChoices):
        HARD = 'HIGH'
        MEDIUM = 'MEDIUM'
        EASY = 'EASY'

    name = models.CharField(max_length=250)
    level = models.CharField(max_length=250,
                             choices=Level.choices,
                             default=Level.MEDIUM)
    distance = models.CharField(max_length=250)
    audience = models.CharField(max_length=250)

    locations = models.ManyToManyField(Location, through='Path')

    def __str__(self):
        return self.name


class Path(models.Model):
    route = models.ForeignKey(Route,
                              on_delete=models.CASCADE)
    location = models.ForeignKey(Location,
                                 on_delete=models.CASCADE)

    order = models.IntegerField()

    class Meta:
        ordering = ['route', 'order']

    def __str__(self):
        return f"{self.route.name} - {self.order}"
