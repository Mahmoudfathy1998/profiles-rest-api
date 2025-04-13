from rest_framework import serializers

from profiles_api import models

# CONTENT SEQ 7th 
class helloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    #All you do is define your serializer and specify the field you wanna accept in ur serializer input.
    name = serializers.CharField(max_length=10) # Creates a new name field in our serializer which is char that allows u to input any char input from your computer that are 10 or less


class UserProfileSerializer(serializers.ModelSerializer): # ModelSerialzers is using a meta class to configure serializers to point to a specific models in our project.
    """Serializes a user profile object"""
   
   
   

    class Meta:
        model = models.UserProfile #Sets up our serializer up to point to our userProfile model
        #Specifiy the list of fields in our model that we want to manage through our serializer. passing a tuble
        
        fields = ('id', 'email', 'name', 'password')
        
        # To make an exception for the password to make it only when creating is through extrakwargs passwords cant be retrieved with a get.
        extra_kwargs = {
            'password': {
                'write_only': True, # means when we create our password field for our model set it to write only which means u can only use it to create/update objects
                'style': {'input_type': 'password'}
            }
        }
    
    
    # Explaination: whenever we create an object using this serializer it will validated the fields provided to the serialzer and it will call this create function. We override the default create function
    # to pass the password hashed instead of a text in the default create function
    def create(self, validated_data):
        """Create and return a new user."""
        user = models.UserProfile.objects.createUser(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        
        return user
    
    
    
class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    
    class Meta:
        model = models.ProfileFeedItem # sets this serializer to this model
        fields = ('id', 'userProfile','statusText','createdOn')
        
        extra_kwargs = {
            'userProfile': {
                'read_only': True, # for user to not being able to create a feed for another user or assign it to another user
            }
        }