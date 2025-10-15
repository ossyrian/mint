"""Base serializers with common functionality."""

from drf_spectacular.extensions import OpenApiSerializerFieldExtension
from drf_spectacular.openapi import AutoSchema
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


class UUIDPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    """
    A related field that uses UUIDs instead of numeric IDs.
    - On read: returns the UUID of the related object
    - On write: looks up objects by their UUID
    """

    def to_internal_value(self, data):
        """Accept UUID for lookups instead of numeric ID."""
        queryset = self.get_queryset()
        try:
            return queryset.get(uuid=data)
        except (TypeError, ValueError, queryset.model.DoesNotExist):
            self.fail("does_not_exist", pk_value=data)

    def to_representation(self, value):
        """Return the UUID instead of the primary key."""
        if hasattr(value, "uuid"):
            return value.uuid  # type:ignore[attr-defined]
        return super().to_representation(value)


class UUIDPrimaryKeyRelatedFieldExtension(OpenApiSerializerFieldExtension):
    """
    OpenAPI schema extension for UUIDPrimaryKeyRelatedField.
    Tells drf-spectacular to document this field as a UUID instead of an integer.
    """

    target_class = "api.serializers.base.UUIDPrimaryKeyRelatedField"

    def map_serializer_field(self, auto_schema: AutoSchema, direction):
        return {
            "type": "string",
            "format": "uuid",
        }


class BaseModelSerializer(FlexFieldsModelSerializer):
    """
    Base serializer that automatically maps 'uuid' field to 'id' in the API.
    Uses UUIDs for all foreign key relationships.
    All model serializers should inherit from this.
    """

    serializer_related_field = UUIDPrimaryKeyRelatedField

    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        abstract = True
