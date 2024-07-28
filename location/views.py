from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer
import os
from django.http import FileResponse

@api_view(['GET'])
def get_data(request):
    items = Location.objects.all()
    serializer = LocationSerializer(items, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@permission_required("location.add_location", raise_exception=True)
def add_data(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def send_audio(request):
    fname = "location/belarusan2_0.wav"
    return FileResponse(open(fname, "rb"), filename=fname)

