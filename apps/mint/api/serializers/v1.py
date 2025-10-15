"""API v1 serializers."""
from minty_hq.models import Guild
from minty_mogul.models import MarketplaceItem
from users.models import User

from api.serializers.base import BaseModelSerializer


class UserSerializerV1(BaseModelSerializer):
    """Version 1 of the User serializer."""

    class Meta:
        model = User
        fields = ["id", "username", "email", "guild", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
        expandable_fields = {
            "guild": ("api.serializers.v1.GuildSerializerV1", {"source": "guild"}),
        }


class GuildSerializerV1(BaseModelSerializer):
    """Version 1 of the Guild serializer."""

    class Meta:
        model = Guild
        fields = [
            "id",
            "name",
            "description",
            "owner",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        expandable_fields = {
            "owner": ("api.serializers.v1.UserSerializerV1", {"source": "owner"}),
        }


class MarketplaceItemSerializerV1(BaseModelSerializer):
    """Version 1 of the MarketplaceItem serializer."""

    class Meta:
        model = MarketplaceItem
        fields = [
            "id",
            "name",
            "description",
            "price",
            "seller",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        expandable_fields = {
            "seller": ("api.serializers.v1.UserSerializerV1", {"source": "seller"}),
        }
