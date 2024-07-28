from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Route, Path
from .serializers import RouteSerializer, RouteInfoSerializer, PathSerializer

# Create your views here.
@api_view(['GET'])
def get_routes(request):
    items = Route.objects.all()
    serializer = RouteSerializer(items, many=True, read_only=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_route_path(request, id):
    item = Path.objects.filter(route__id=id)
    route_serializer = PathSerializer(item, many=True, read_only=True)
    return Response(data=route_serializer.data)
