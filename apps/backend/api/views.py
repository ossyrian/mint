from rest_framework import viewsets
from .models import Item, Guild, User
from .serializers import get_item_serializer, get_guild_serializer, get_user_serializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for items. Version-agnostic view.
    """

    queryset = Item.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_item_serializer(version)


class GuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint for guilds. Version-agnostic view.
    """

    queryset = Guild.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_guild_serializer(version)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users. Version-agnostic view.
    """

    queryset = User.objects.all()
    lookup_field = 'uuid'

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_user_serializer(version)
