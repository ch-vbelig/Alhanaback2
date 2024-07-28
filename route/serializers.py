from rest_framework import serializers
from .models import Route, Path
from location.serializers import LocationSerializer

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'name', 'level', 'distance']


class RouteInfoSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)
    class Meta:
        model = Route
        fields = ['name', 'locations']

class PathSerializer(serializers.ModelSerializer):

    location = LocationSerializer(many=False, read_only=True)

    class Meta:
        model = Path
        fields = '__all__'
