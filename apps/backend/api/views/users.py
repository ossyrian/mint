from rest_framework import viewsets

from api.models import User
from api.serializers import (
    get_user_serializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users. Version-agnostic view.
    """

    queryset = User.objects.all()
    lookup_field = "uuid"

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_user_serializer(version)
