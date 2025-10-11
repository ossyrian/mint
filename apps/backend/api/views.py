from rest_framework import viewsets
from .models import Item
from .serializers import get_item_serializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for items. Version-agnostic view.
    """

    queryset = Item.objects.all()

    def get_serializer_class(self):
        """
        Return the appropriate serializer based on API version.
        """
        version = self.request.version or "v1"
        return get_item_serializer(version)
