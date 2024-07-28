from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes),
    path('<int:id>', views.get_route_path)
]