from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='about'),
]