from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
# Create your models here.

class userProfile(AbstractBaseUser , PermissionsMixin):
    """
    this class defines the custom user
    """
    
