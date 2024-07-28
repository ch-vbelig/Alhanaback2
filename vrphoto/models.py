from django.db import models
from location.models import Location
# Create your models here.


class VRPhoto(models.Model):

    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        related_name='vrphoto'
    )
    url = models.ImageField(null=True, upload_to='vr_images/')

    def __str__(self):
        return self.location.name

