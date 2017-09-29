from django.conf.urls import url , include
from django.contrib import admin
from rest_framework.routers import DefaultRouter 
from .views import HelloApiView ,UserProfileView , BookView , LoginViewset

router = DefaultRouter()
router.register('profile' , UserProfileView)
router.register('book' , BookView)
router.register('login' , LoginViewset , base_name="login")


urlpatterns = [
    
    url(r'^hello', view = HelloApiView.as_view()),
    url(r'^', include(router.urls)),
    

]