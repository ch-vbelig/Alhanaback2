from rest_framework import serializers
from vrphoto.models import VRPhoto

class VRPhotoSerializer(serializers.ModelSerializer):
    url = serializers.ImageField(use_url=True)

    class Meta:
        model = VRPhoto
        fields = ['url', 'location']


class VRPhotoSaveSerializer(serializers.ModelSerializer):
    url = serializers.ImageField()

    class Meta:
        model = VRPhoto
        fields = ['location', 'url']