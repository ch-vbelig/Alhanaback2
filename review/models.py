from django.db import models
from location.models import Location
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        split = 25
        return (str(self.text[0:split]) + '...') if len(str(self.text)) > split else self.text

