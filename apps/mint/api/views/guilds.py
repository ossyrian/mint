from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from minty_hq.models import Guild
from api.serializers.v1 import GuildSerializerV1


@extend_schema_view(
    list=extend_schema(tags=["MintyHQ"]),
    retrieve=extend_schema(tags=["MintyHQ"]),
    create=extend_schema(tags=["MintyHQ"]),
    update=extend_schema(tags=["MintyHQ"]),
    partial_update=extend_schema(tags=["MintyHQ"]),
    destroy=extend_schema(tags=["MintyHQ"]),
)
class GuildViewSet(viewsets.ModelViewSet):
    """API endpoint for guilds."""

    queryset = Guild.objects.all()
    serializer_class = GuildSerializerV1
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["owner"]
    ordering_fields = ["name", "created_at"]
