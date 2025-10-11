"""API v1 serializers."""
from rest_framework import serializers
from ..models import Item, Guild, User


class UserSerializerV1(serializers.ModelSerializer):
    """Version 1 of the User serializer."""
    id = serializers.UUIDField(source='uuid', read_only=True)
    guild_id = serializers.UUIDField(source='guild.uuid', read_only=True, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'guild_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class GuildSerializerV1(serializers.ModelSerializer):
    """Version 1 of the Guild serializer."""
    id = serializers.UUIDField(source='uuid', read_only=True)
    owner_id = serializers.UUIDField(source='owner.uuid', read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Guild
        fields = ['id', 'name', 'description', 'owner_id', 'owner_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class ItemSerializerV1(serializers.ModelSerializer):
    """Version 1 of the Item serializer."""
    id = serializers.UUIDField(source='uuid', read_only=True)
    seller_id = serializers.UUIDField(source='seller.uuid', read_only=True)
    seller_username = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'seller_id', 'seller_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
