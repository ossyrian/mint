"""Game data serializers for API v1."""
from rest_framework import serializers

from api.models.game.characters import Job, MapleClass, Skill
from api.models.game.crafting import CraftingIngredient, CraftingRecipe
from api.models.game.items import Item, ItemDrop
from api.models.game.mobs import Mob, MobSpawn
from api.models.game.npcs import NPC, NPCLocation, NPCShopItem
from api.models.game.quests import Quest, QuestReward
from api.models.game.world import Continent, Map, Region
from api.serializers.base import BaseModelSerializer


class MapleClassSerializer(BaseModelSerializer):
    class Meta:
        model = MapleClass
        fields = ["id", "source_id", "name", "description"]


class JobSerializer(BaseModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "source_id", "name", "description", "maple_class"]
        expandable_fields = {"maple_class": (MapleClassSerializer, {"source": "maple_class"})}


class SkillSerializer(BaseModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "source_id", "name", "description", "job"]
        expandable_fields = {"job": (JobSerializer, {"source": "job"})}


class ItemSerializer(BaseModelSerializer):
    class Meta:
        model = Item
        fields = [
            "id",
            "source_id",
            "name",
            "description",
            "slot",
            "category",
            "subcategory",
            "attributes",
        ]


class MobSerializer(BaseModelSerializer):
    class Meta:
        model = Mob
        fields = ["id", "source_id", "name", "description", "hp", "mp", "exp", "mesos"]


class ContinentSerializer(BaseModelSerializer):
    class Meta:
        model = Continent
        fields = ["id", "source_id", "name", "description"]


class RegionSerializer(BaseModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "source_id", "name", "description", "continent"]
        expandable_fields = {"continent": (ContinentSerializer, {"source": "continent"})}


class MapSerializer(BaseModelSerializer):
    class Meta:
        model = Map
        fields = ["id", "source_id", "name", "description", "region"]
        expandable_fields = {"region": (RegionSerializer, {"source": "region"})}


class NPCSerializer(BaseModelSerializer):
    class Meta:
        model = NPC
        fields = ["id", "source_id", "name", "description"]


class QuestSerializer(BaseModelSerializer):
    class Meta:
        model = Quest
        fields = [
            "id",
            "source_id",
            "name",
            "description",
            "quest_line",
            "started_by",
            "meso_reward",
            "exp_reward",
            "prerequisite_quest",
            "required_level",
            "required_class",
            "required_job",
            "misc_requirements",
        ]
        expandable_fields = {
            "started_by": (NPCSerializer, {"source": "started_by"}),
            "prerequisite_quest": (
                "api.serializers.game_v1.QuestSerializer",
                {"source": "prerequisite_quest"},
            ),
            "required_class": (MapleClassSerializer, {"source": "required_class"}),
            "required_job": (JobSerializer, {"source": "required_job"}),
        }


class CraftingRecipeSerializer(BaseModelSerializer):
    class Meta:
        model = CraftingRecipe
        fields = [
            "id",
            "result_item",
            "result_quantity",
            "meso_cost",
            "crafter_npc",
        ]
        expandable_fields = {
            "result_item": (ItemSerializer, {"source": "result_item"}),
            "crafter_npc": (NPCSerializer, {"source": "crafter_npc"}),
        }


class ItemDropSerializer(BaseModelSerializer):
    class Meta:
        model = ItemDrop
        fields = ["id", "item", "mob", "drop_rate"]
        expandable_fields = {
            "item": (ItemSerializer, {"source": "item"}),
            "mob": (MobSerializer, {"source": "mob"}),
        }


class MobSpawnSerializer(BaseModelSerializer):
    class Meta:
        model = MobSpawn
        fields = ["id", "mob", "map"]
        expandable_fields = {
            "mob": (MobSerializer, {"source": "mob"}),
            "map": (MapSerializer, {"source": "map"}),
        }


class NPCLocationSerializer(BaseModelSerializer):
    class Meta:
        model = NPCLocation
        fields = ["id", "npc", "map"]
        expandable_fields = {
            "npc": (NPCSerializer, {"source": "npc"}),
            "map": (MapSerializer, {"source": "map"}),
        }


class NPCShopItemSerializer(BaseModelSerializer):
    class Meta:
        model = NPCShopItem
        fields = ["id", "npc", "item", "price"]
        expandable_fields = {
            "npc": (NPCSerializer, {"source": "npc"}),
            "item": (ItemSerializer, {"source": "item"}),
        }


class QuestRewardSerializer(BaseModelSerializer):
    class Meta:
        model = QuestReward
        fields = ["id", "quest", "item", "quantity", "reward_group"]
        expandable_fields = {
            "quest": (QuestSerializer, {"source": "quest"}),
            "item": (ItemSerializer, {"source": "item"}),
        }


class CraftingIngredientSerializer(BaseModelSerializer):
    class Meta:
        model = CraftingIngredient
        fields = ["id", "recipe", "item", "quantity"]
        expandable_fields = {
            "recipe": (CraftingRecipeSerializer, {"source": "recipe"}),
            "item": (ItemSerializer, {"source": "item"}),
        }
