from rest_framework import permissions

from mysite.settings import INTERNAL_API_KEY


class IsInternal(permissions.BasePermission):

    def has_permission(self, request, view):
        api_key = None

        api_key = request.META.get(
                'HTTP_AUTHORIZATION', None
            )

        if not api_key:
            if request.method == 'GET':
                api_key = request.GET.get('api_key', None)
            else:
                api_key = request.DATA.get('api_key', None)

        return api_key == INTERNAL_API_KEY