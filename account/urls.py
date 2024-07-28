from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user),
    path('signup/', views.signup_user),
    path('test/', views.test_user),
]