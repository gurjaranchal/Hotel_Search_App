from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name="home"),
    path('api/hotels',api_hotels),
    path('about/',aboutus,name="about"),
    path('facility/',facility,name="facility"),
]