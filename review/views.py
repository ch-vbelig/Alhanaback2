from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from location.models import Location
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
@api_view(['GET'])
def get_reviews(request):
    items = Review.objects.all()
    serializer = ReviewSerializer(items, many=True, read_only=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_review(request, id):
    item = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(item, many=False, read_only=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_review_for_location(request, id):
    items = get_list_or_404(Review, location__id=id)
    serializer = ReviewSerializer(items, many=True, read_only=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_review_for_location(request):
    print("POST")
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        r = serializer.save()
        item = Review.objects.get(id=r.id)
        review = ReviewSerializer(item, many=False, read_only=True)
        return Response(review.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_review_for_location(request):
    print("POST")
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid():
        r = serializer.save()
        item = Review.objects.get(id=r.id)
        review = ReviewSerializer(item, many=False, read_only=True)
        return Response(review.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
