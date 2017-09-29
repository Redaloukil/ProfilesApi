from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import UserProfilesSerializer , ApiStartSerializer , BookSerializer
from .models import UserProfile , Book
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = ApiStartSerializer
    
    def get(self , request , format = None):
        an_apiview = [
            "Uses Http Method as function(get , post , patch , put , delete)"

        ]
        return Response({'message':'Hello!','an_apiview':an_apiview })

    def post(self , request):
        """Create a hello message with our name"""

        serial =ApiStartSerializer(data = request.data)

        if serial.is_valid() :
            username = serial.data.get("username")
            message = 'Hello %s'%format(username)
            return Response({
                'message':message
            })
        else :
            return Response(
                serial.errors , status= status.HTTP_400_BAD_REQUEST
            )

    def put(self , request , pk = None):

        return Response({"method" : 'put'})


    def patch(self , request , pk = None):

        return Response({"method" : 'patch'})

    def delete(self , request , pk = None):

        return Response({"method" : 'delete'})

class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfilesSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name' , 'email')

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LoginViewset(viewsets.ViewSet):
    
    serializer_class = AuthTokenSerializer
    
    def create(self , request):
        return ObtainAuthToken.post(request)