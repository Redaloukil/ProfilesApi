from django.conf.urls import url , include
from django.contrib import admin
from rest_framework.routers import DefaultRouter 
from .views import HelloApiView 



urlpatterns = [
    
    url(r'^hello', view = HelloApiView.as_view()),

]