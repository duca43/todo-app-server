from rest_framework.permissions import BasePermission

class TodoAccessPermission(BasePermission):

    message = 'You cannot access this todo.'
    
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        return False
