from django.contrib import admin
from django.urls import path

from .views import CustomCard

urlpatterns = [
    path('<slug:slug>', CustomCard.as_view(), name='cards')
] 