from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class permission(BasePermission):

    def has_authentication(self,request,view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return True
        else:
            return False