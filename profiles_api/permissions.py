from rest_framework import permissions # provides base class to use to create custom permission class


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    
    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        #everytime a request is made DRF calls this function passing the request,view and the obj we are checking permissions against
        if request.method in permissions.SAFE_METHODS: #methods that dont make any changes to an object http GET for ex
            return True
        
        return obj.id == request.user.id #if the the user is trying to update their own profile returns True
    
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.userProfile.id == request.user.id