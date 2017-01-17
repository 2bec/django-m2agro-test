from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super(IsAuthenticatedOrReadOnly, self).has_permission(request, view)