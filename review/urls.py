from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_reviews),
    path('<int:id>', views.get_review),
    path('location/<int:id>', views.get_review_for_location),
    path('location/save', views.save_review_for_location)
]