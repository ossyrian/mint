from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from api.models.game.characters import Job, MapleClass, Skill
from api.models.game.crafting import CraftingRecipe
from api.models.game.items import Item
from api.models.game.mobs import Mob
from api.models.game.npcs import NPC
from api.models.game.quests import Quest
from api.models.game.world import Continent, Map, Region
from api.serializers.game_v1 import (
    ContinentSerializer,
    CraftingIngredientSerializer,
    CraftingRecipeSerializer,
    ItemDropSerializer,
    ItemSerializer,
    JobSerializer,
    MapleClassSerializer,
    MapSerializer,
    MobSerializer,
    MobSpawnSerializer,
    NPCLocationSerializer,
    NPCSerializer,
    NPCShopItemSerializer,
    QuestRewardSerializer,
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
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.with_class()  # type:ignore[attr-defined]
    serializer_class = JobSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["maple_class"]
    ordering_fields = ["name"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.with_job()  # type:ignore[attr-defined]
    serializer_class = SkillSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["job"]
    ordering_fields = ["name"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["slot", "category", "subcategory"]
    ordering_fields = ["name", "slot", "category"]

    @extend_schema(tags=["MintyDB"], responses={200: ItemDropSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def dropped_by(self, request, uuid=None):
        item = self.get_object()
        drops = item.itemdrop_set.select_related("mob").order_by("-drop_rate")
        serializer = ItemDropSerializer(drops, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: NPCShopItemSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def sold_by(self, request, uuid=None):
        item = self.get_object()
        shops = item.npcshopitem_set.select_related("npc").order_by("price")
        serializer = NPCShopItemSerializer(shops, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: CraftingIngredientSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def used_in_recipes(self, request, uuid=None):
        item = self.get_object()
        ingredients = item.craftingingredient_set.select_related(
            "recipe__result_item"
        ).order_by("recipe__result_item__name")
        serializer = CraftingIngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: QuestRewardSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def quest_rewards(self, request, uuid=None):
        item = self.get_object()
        rewards = item.questreward_set.select_related("quest").order_by(
            "reward_group", "quest__name"
        )
        serializer = QuestRewardSerializer(rewards, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class MobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Mob.objects.all()
    serializer_class = MobSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["hp", "exp", "mesos"]
    ordering_fields = ["name", "hp", "exp", "mesos"]

    @extend_schema(tags=["MintyDB"], responses={200: ItemDropSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def drops(self, request, uuid=None):
        mob = self.get_object()
        drops = mob.itemdrop_set.select_related("item").order_by("-drop_rate")
        serializer = ItemDropSerializer(drops, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: MobSpawnSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def spawns(self, request, uuid=None):
        mob = self.get_object()
        spawns = mob.mobspawn_set.select_related(
            "map__region__continent"
        ).order_by("map__name")
        serializer = MobSpawnSerializer(spawns, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class ContinentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.with_continent()  # type:ignore[attr-defined]
    serializer_class = RegionSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["continent"]
    ordering_fields = ["name"]


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class MapViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Map.objects.with_region()  # type:ignore[attr-defined]
    serializer_class = MapSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["region"]
    ordering_fields = ["name"]

    @extend_schema(tags=["MintyDB"], responses={200: MobSpawnSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def mobs(self, request, uuid=None):
        map_obj = self.get_object()
        spawns = map_obj.mobspawn_set.select_related("mob").order_by("mob__name")
        serializer = MobSpawnSerializer(spawns, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: NPCLocationSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def npcs(self, request, uuid=None):
        map_obj = self.get_object()
        locations = map_obj.npclocation_set.select_related("npc").order_by("npc__name")
        serializer = NPCLocationSerializer(locations, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class NPCViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]

    @extend_schema(tags=["MintyDB"], responses={200: NPCShopItemSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def sells(self, request, uuid=None):
        npc = self.get_object()
        items = npc.npcshopitem_set.select_related("item").order_by("price")
        serializer = NPCShopItemSerializer(items, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: NPCLocationSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def locations(self, request, uuid=None):
        npc = self.get_object()
        locations = npc.npclocation_set.select_related(
            "map__region__continent"
        ).order_by("map__name")
        serializer = NPCLocationSerializer(locations, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: QuestSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def quests(self, request, uuid=None):
        npc = self.get_object()
        quests = npc.quests.order_by("name")
        serializer = QuestSerializer(quests, many=True)
        return Response(serializer.data)

    @extend_schema(tags=["MintyDB"], responses={200: CraftingRecipeSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def recipes(self, request, uuid=None):
        npc = self.get_object()
        recipes = npc.crafting_recipes.select_related("result_item").order_by(
            "result_item__name"
        )
        serializer = CraftingRecipeSerializer(recipes, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class QuestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quest.objects.with_requirements()  # type:ignore[attr-defined]
    serializer_class = QuestSerializer
    lookup_field = "uuid"
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["quest_line", "required_level", "required_class", "required_job", "started_by"]
    ordering_fields = ["name", "required_level"]

    @extend_schema(tags=["MintyDB"], responses={200: QuestRewardSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def rewards(self, request, uuid=None):
        quest = self.get_object()
        rewards = quest.questreward_set.select_related("item").order_by(
            "reward_group", "item__name"
        )
        serializer = QuestRewardSerializer(rewards, many=True)
        return Response(serializer.data)


@extend_schema_view(
    list=extend_schema(tags=["MintyDB"]),
    retrieve=extend_schema(tags=["MintyDB"]),
)
class CraftingRecipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CraftingRecipe.objects.with_result()  # type:ignore[attr-defined]
    serializer_class = CraftingRecipeSerializer
    lookup_field = "uuid"
    filter_backends = [OrderingFilter]
    filterset_fields = ["result_item", "crafter_npc", "meso_cost"]
    ordering_fields = ["result_item__name", "meso_cost"]

    @extend_schema(tags=["MintyDB"], responses={200: CraftingIngredientSerializer(many=True)})
    @action(detail=True, methods=["get"])
    def ingredients(self, request, uuid=None):
        recipe = self.get_object()
        ingredients = recipe.craftingingredient_set.select_related("item").order_by(
            "item__name"
        )
        serializer = CraftingIngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
