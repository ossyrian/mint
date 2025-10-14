from rest_framework import viewsets

from api.models import MarketplaceItem
from api.serializers import get_item_serializer


class MarketplaceItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for items. Version-agnostic view.
    """

    queryset = MarketplaceItem.objects.all()
    lookup_field = "uuid"

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_item_serializer(version)
