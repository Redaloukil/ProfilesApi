from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

# Create your models here.

class userProfileManager(BaseUserManager):
    """
        this object will take control of userProfile model.
    """

class userProfile(AbstractBaseUser , PermissionsMixin):
    """
    this class defines the custom user
    """
    email = models.EmailField(max_length=55,blank =False , unique = True )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    #define our model manager
    objects = userProfileManager()

    #replacing username as required field to email 
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["email" , "first_name" , "last_name"]

    # using this method to get first name
    def get_firstName(self):
        return self.first_name
    # using this method to get last name
    def get_lastName(self):
        return self.last_name
    # using this method to get email
    def get_email(self):
        return self.email
    # using this method to get the name of the object
    def __str__(self):
        return self.email