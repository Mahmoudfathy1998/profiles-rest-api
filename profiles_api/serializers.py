from rest_framework import serializers

# CONTENT SEQ 7th 
class helloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    #All you do is define your serializer and specify the field you wanna accept in ur serializer input.
    name = serializers.CharField(max_length=10) # Creates a new name field in our serializer which is char that allows u to input any char input from your computer that are 10 or less
