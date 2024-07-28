from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.decorators import permission_required
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import VRPhoto
from .serializers import VRPhotoSerializer, VRPhotoSaveSerializer


# Create your views here.
@api_view(['GET'])
def get_vr_photos(request):
    items = VRPhoto.objects.all()
    serializer = VRPhotoSerializer(items, many=True, read_only=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_vr_photo(request, id):
    vrphoto = VRPhoto.objects.get(id=id)
    serializer = VRPhotoSerializer(vrphoto, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@permission_required("vrphoto.add_vrphoto", raise_exception=True)
def upload_vr_photo(request):
    location_id = request.data['location_id']
    file = request.data['url']

    serializer = VRPhotoSaveSerializer(data={
        "location": location_id,
        "url": file
    })

    if serializer.is_valid():
        serializer.save()
        return Response({
            "url": serializer.data['url']
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)