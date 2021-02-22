from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serialzers
from profiles_api import models
from profiles_api import permission


class HelloApiView(APIView):
    """Test Api View"""
    serialzers_class = serialzers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list APiView features"""
        an_apiView = [
            'Uses HTTP methods ad Function (get ,post , patch,put,delete)',
            'Is Similar to a traditional Django view',
            'Gives you the most control over the application',
            'Is mapped maually to Urls',
            'This is a Good',
        ]
        return Response({'message': "Hello", 'an_ApiView': an_apiView})
    
    def post(self,request):
        """Create a hello message with our name"""
        serialzers = self.serialzers_class(data=request.data)
        if serialzers.is_valid():
            name = serialzers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serialzers.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating object"""
        return Response({'method':"Put"})

    def patch(self,request,pk = None):
        """Handle a partial update of an object"""
        return Response({'method':"Patch"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":'this delete the object'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serialzers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle Creating user auth tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating and reading profile feeds items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serialzers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permission.UpdateOwnStatus,
        IsAuthenticated

    
    )
 
    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile = self.request.user)





