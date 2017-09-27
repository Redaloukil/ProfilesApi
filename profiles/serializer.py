from rest_framework.serializers import ModelSerializer
from .models import UserProfile
from rest_framework import serializers


class UserProfilesSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id' , 'email','name','is_staff','is_active')

        def create(self , request ):
            user = UserProfile(
                email = request["email"],
                name = request["name"]
            )

            user.set_password(request["password"])
            user.save()

            return user 

class ApiStartSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 20)
    

