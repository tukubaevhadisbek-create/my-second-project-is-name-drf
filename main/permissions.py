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

        return obj.employer.user == request.user


class IsApplicantOrReadOnly(BasePermission):

    def has_permission(self, request, view):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return (
            request.user.is_authenticated
            and hasattr(request.user, 'applicant')
        )

    def has_object_permission(self, request, view, obj):

        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        return obj.applicant.user == request.user


class IsApplicant(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, 'applicant')
        )


class IsEmployer(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, 'employer')
        )