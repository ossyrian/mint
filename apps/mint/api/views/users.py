from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from users.models import User
from api.serializers.v1 import UserSerializerV1


@extend_schema_view(
    list=extend_schema(tags=["Users"]),
    retrieve=extend_schema(tags=["Users"]),
    create=extend_schema(tags=["Users"]),
    update=extend_schema(tags=["Users"]),
    partial_update=extend_schema(tags=["Users"]),
    destroy=extend_schema(tags=["Users"]),
)
class UserViewSet(viewsets.ModelViewSet):
    """API endpoint for users."""

    queryset = User.objects.all()
    serializer_class = UserSerializerV1
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["username", "email"]
    filterset_fields = ["guild"]
    ordering_fields = ["username", "created_at"]
