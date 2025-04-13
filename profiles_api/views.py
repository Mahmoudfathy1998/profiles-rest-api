from rest_framework.views import APIView
from rest_framework.response import Response #GET usage.
from rest_framework import status #POST  usage.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly ,IsAuthenticated

from profiles_api import serializers #POST usage.
from profiles_api import models
from profiles_api import permissions

# CONTENT SEQ 5th create apiview.
#Creates a new class that's based on the djangorest apiview class
class HelloApiView(APIView):
    """Test API view"""
    
    #to Tell our apiview what data to expect when making post, put, patch request to our API
    serializer_class = serializers.helloSerializer #Configures our APIView to have this serialzer class.
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiView = ['Uses HTTP methods as function (get, post, patch, put, delete)',
                   'Is similar to a traditional Django view',
                   'Gives you the most control over your app logic',
                   'Is mapped manually to URLs',
                   ]
        
        return Response({'message': 'Hello!',
                         'apiView': apiView})
        

# CONTENT SEQ 8th
    def post(self, request):
        """Create a hello message with our name"""
        # Retrieve the serializer and pass in the data that was sent in the request
        serializer = self.serializer_class(data=request.data) #This is a function that comes with APIView that retireves the configured serializer class for our view.
        
        if serializer.is_valid(): #Validates the serialzer.
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,#gives u a dict of all the errors when validation happened
                status=status.HTTP_400_BAD_REQUEST,
                ) 
    
    # CONTENT SEQ 9th
    def put(self, request, pk=None): # PrimaryKey of the object to be updated.
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
    
    
# CONTENT SEQ 10th Can be replaced with CONTENT SEQ 5th
class HelloViewSet(viewsets.ViewSet): #.viewset is the base django viewset class that django provides
    """Test API ViewSet"""
    
    def list(self, request):
        """Return a hello message."""
        viewsetList = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically mapts to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({
            'message': 'Hello!',
            'viewSetList': viewsetList
            });
    
    def create(self, request):
        """Create a new hello message"""
        userData = request.data
        message = f'Hello {userData.get('name')}'
        return Response({
            'message': message
        })
        
    
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({
            'httpMethod': 'GET'
        })
        
        
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({
            'httpMethod': f'PUT {request.data.get('name')}'
        })
        
        
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({
            'httpMethod': 'PATCH'
        })
        
        
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({
            'httpMethod': 'DELETE'
        })
        
        
class UserProfileViewSet(viewsets.ModelViewSet): # To use the model view set is to connect it to up to a serializer class and provide a query set to the modelviewset 
    """Handle creating and updating profiles"""
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all() #DRF knows the standard funcs that you want to perform on the model viewset create,list,update,partial_update,destroy just by assigning these <- 
    # How the user will authenticate
    authentication_classes = (TokenAuthentication, ) # Remember to add comma after token auth as its a tuple. This adds all the auth classes to this variable
    #How the user gets permission to do certain things.
    permission_classes = (permissions.UpdateOwnProfile,)
    # Adding a filter backend for the search filter and then specify the search fields
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email', )
    
    
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    #adds the rendere classes to the obtainauthtoken which will enable it in the django admin as obtainAuthToken doesnt have it bydefault
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating,reading,updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()#manage all of our profileFeedItem objects from a model in our viewset
    permission_classes = (
        permissions.UpdateOwnStatus,
        #IsAuthenticatedOrReadOnly #This makes sure that a user must be authenticated perform anyrequest that's not a read request. User cannot create a new feeditem if they'rent authenticated
        IsAuthenticated # used in case no access to the read only requests as well
    )
    
    #This is a handy feature in DRF that allows you to override/customize the behavior for creating an object for a modelviewset, When a request is made to the viewset it get passed into
    #our serializer class and validate it and then serilaizer.save is called by default.
    # This is called everytime you do HTTP POST to the viewset
    def perform_create(self, serializer):
        #we did this in order to apply the readonly for the userprofile attr
        """Sets the user profile to the logged in user."""
        serializer.save(userProfile=self.request.user) #request is passed by defualt for the viewsets and if the user is authenticated. user will be added to the request, this user_profile pass to the serializer
                                                        #in addition to the items that's being passed to it thats being validated
        