"""
Versioned serializers for the API.

Import the appropriate serializer based on the API version.
"""
from .v1 import ItemSerializerV1, GuildSerializerV1, UserSerializerV1


def get_item_serializer(version):
    """Return the appropriate item serializer for the given API version."""
    serializers = {
        'v1': ItemSerializerV1,
    }
    return serializers.get(version, ItemSerializerV1)


def get_guild_serializer(version):
    """Return the appropriate guild serializer for the given API version."""
    serializers = {
        'v1': GuildSerializerV1,
    }
    return serializers.get(version, GuildSerializerV1)


def get_user_serializer(version):
    """Return the appropriate user serializer for the given API version."""
    serializers = {
        'v1': UserSerializerV1,
    }
    return serializers.get(version, UserSerializerV1)
