from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_video, name="upload"),
    path('success/', views.successPage, name="success"),
    path('error/', views.errorPage, name="error"),
]