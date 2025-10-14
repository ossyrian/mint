"""Base serializers with common functionality."""
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


class BaseModelSerializer(FlexFieldsModelSerializer):
    """
    Base serializer that automatically maps 'uuid' field to 'id' in the API.
    All model serializers should inherit from this.
    """

    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        abstract = True
