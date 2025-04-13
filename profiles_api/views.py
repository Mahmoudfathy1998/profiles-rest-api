from rest_framework.views import APIView
from rest_framework.response import Response #GET usage.
from rest_framework import status #POST  usage.
from rest_framework import viewsets

from profiles_api import serializers #POST usage.

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