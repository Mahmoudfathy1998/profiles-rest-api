from rest_framework.views import APIView
from rest_framework.response import Response

# CONTECT SEQ 5th create apiview.
#Creates a new class that's based on the djangorest apiview class
class HelloApiView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        apiView = ['Uses HTTP methods as function (get, post, patch, put, delete)',
                   'Is similar to a traditional Django view',
                   'Gives you the most control over your app logic',
                   'Is mapped manually to URLs',
                   ]
        
        return Response({'message': 'Hello!',
                         'apiView': apiView})