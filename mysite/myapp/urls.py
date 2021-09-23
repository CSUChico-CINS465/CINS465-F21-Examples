from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('useful/', views.delete_random),
]