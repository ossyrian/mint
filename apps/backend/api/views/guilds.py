from rest_framework import viewsets

from api.models import Guild
from api.serializers import (
    get_guild_serializer,
)


class GuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint for guilds. Version-agnostic view.
    """

    queryset = Guild.objects.all()
    lookup_field = "uuid"

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_guild_serializer(version)
