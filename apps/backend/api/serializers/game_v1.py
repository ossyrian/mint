"""Game data serializers for API v1."""
from rest_flex_fields import FlexFieldsModelSerializer

from api.models.game.characters import Job, MapleClass, Skill
from api.models.game.crafting import CraftingIngredient, CraftingRecipe
from api.models.game.items import Item, ItemDrop
from api.models.game.mobs import Mob, MobSpawn
from api.models.game.npcs import NPC, NPCLocation, NPCShopItem
from api.models.game.quests import Quest, QuestReward
from api.models.game.world import Continent, Map, Region


class MapleClassSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = MapleClass
        fields = ["uuid", "source_id", "name", "description"]


class JobSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Job
        fields = ["uuid", "source_id", "name", "description", "maple_class"]
        expandable_fields = {"maple_class": (MapleClassSerializer, {"source": "maple_class"})}


class SkillSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Skill
        fields = ["uuid", "source_id", "name", "description", "job"]
        expandable_fields = {
            "job": (JobSerializer, {"source": "job"}),
        }


class ItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Item
        fields = [
            "uuid",
            "source_id",
            "name",
            "description",
            "slot",
            "category",
            "subcategory",
            "attributes",
        ]


class MobSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Mob
        fields = ["uuid", "source_id", "name", "description", "hp", "mp", "exp", "mesos"]


class ContinentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Continent
        fields = ["uuid", "source_id", "name", "description"]


class RegionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Region
        fields = ["uuid", "source_id", "name", "description", "continent"]
        expandable_fields = {
            "continent": (ContinentSerializer, {"source": "continent"}),
        }


class MapSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Map
        fields = ["uuid", "source_id", "name", "description", "region"]
        expandable_fields = {
            "region": (RegionSerializer, {"source": "region"}),
        }


class NPCSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = NPC
        fields = ["uuid", "source_id", "name", "description"]


class QuestSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Quest
        fields = [
            "uuid",
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


class CraftingRecipeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = CraftingRecipe
        fields = [
            "uuid",
            "source_id",
            "name",
            "description",
            "result_item",
            "result_quantity",
            "meso_cost",
            "crafter_npc",
        ]
        expandable_fields = {
            "result_item": (ItemSerializer, {"source": "result_item"}),
            "crafter_npc": (NPCSerializer, {"source": "crafter_npc"}),
        }
