from django.conf.urls import url , include
from django.contrib import admin
from rest_framework.routers import DefaultRouter 
from .views import HelloApiView ,userProfileView

router = DefaultRouter()
router.register('profile' , userProfileView)

urlpatterns = [
    
    url(r'^/hello', view = HelloApiView.as_view()),
    url(r'^/', include(router.urls)),

]