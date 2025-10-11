"""API v1 serializers."""
from rest_framework import serializers
from ..models import Item


class ItemSerializerV1(serializers.ModelSerializer):
    """Version 1 of the Item serializer."""
    seller_username = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'price', 'seller', 'seller_username', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
