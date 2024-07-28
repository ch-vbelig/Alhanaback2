from rest_framework import serializers
from location.models import Location
from vrphoto.serializers import VRPhotoSerializer

class LocationSerializer(serializers.ModelSerializer):
    # vrphoto = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='vrphoto-detail',
    #     lookup_field='id'
    # )
    vrphoto = VRPhotoSerializer(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'description', 'latitude', 'longitude', 'vrphoto']