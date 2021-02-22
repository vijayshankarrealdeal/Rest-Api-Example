from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own Profile"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own permission"""
    def has_object_permission(self,request,view,obj):
        """check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id
