from rest_framework.serializers import ModelSerializer
from .models import UserProfile , Book
from rest_framework import serializers

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id' , 'owner','name','author','describ',)

        def create(self , request ):
            book = Book(
                owner = request.user["username"],
                name = request["name"],
                author = request["author"],
                describ = request["describ"],
            )
            Book.save()
            return book
class UserProfilesSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id' , 'email','name','password','is_staff','is_active')

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
    

