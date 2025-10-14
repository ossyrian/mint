from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from api.models.game.characters import Job, MapleClass, Skill
from api.models.game.crafting import CraftingRecipe
from api.models.game.items import Item
from api.models.game.mobs import Mob
from api.models.game.npcs import NPC
from api.models.game.quests import Quest
from api.models.game.world import Continent, Map, Region
from api.serializers.game_v1 import (
    ContinentSerializer,
    CraftingRecipeSerializer,
    ItemSerializer,
    JobSerializer,
    MapleClassSerializer,
    MapSerializer,
    MobSerializer,
    NPCSerializer,
    QuestSerializer,
    RegionSerializer,
    SkillSerializer,
)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class MapleClassViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MapleClass.objects.all()
    serializer_class = MapleClassSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.with_class()  # type:ignore[attr-defined]
    serializer_class = JobSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.with_job()  # type:ignore[attr-defined]
    serializer_class = SkillSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "uuid"
    filterset_fields = ["slot", "category", "subcategory"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class MobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mob.objects.all()
    serializer_class = MobSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.with_continent()  # type:ignore[attr-defined]
    serializer_class = RegionSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class MapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Map.objects.with_region()  # type:ignore[attr-defined]
    serializer_class = MapSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class NPCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer
    lookup_field = "uuid"


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class QuestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quest.objects.with_requirements()  # type:ignore[attr-defined]
    serializer_class = QuestSerializer
    lookup_field = "uuid"
    filterset_fields = ["quest_line"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class CraftingRecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CraftingRecipe.objects.with_result()  # type:ignore[attr-defined]
    serializer_class = CraftingRecipeSerializer
    lookup_field = "uuid"
