from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_vr_photos),
    path('<int:id>', views.get_vr_photo),
    path('add/', views.upload_vr_photo)
]