from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission


class IsEmployerOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return (
            request.user.is_authenticated
            and hasattr(request.user, 'employer')
        )

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if request.method == 'DELETE':
            return obj.user == request.user

        return True

class IsApplicantOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return (
            request.user.is_authenticated
            and hasattr(request.user, 'applicant')
        )
    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        if request.method == 'DELETE':
            return obj.user == request.user

        return True

