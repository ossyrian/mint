from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from minty_mogul.models import MarketplaceItem
from api.serializers.v1 import MarketplaceItemSerializerV1


@extend_schema_view(
    list=extend_schema(tags=["MintyMogul"]),
    retrieve=extend_schema(tags=["MintyMogul"]),
    create=extend_schema(tags=["MintyMogul"]),
    update=extend_schema(tags=["MintyMogul"]),
    partial_update=extend_schema(tags=["MintyMogul"]),
    destroy=extend_schema(tags=["MintyMogul"]),
)
class MarketplaceItemViewSet(viewsets.ModelViewSet):
    """API endpoint for marketplace items."""

    queryset = MarketplaceItem.objects.all()
    serializer_class = MarketplaceItemSerializerV1
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["seller", "price"]
    ordering_fields = ["name", "price", "created_at"]
