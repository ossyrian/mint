from django.contrib import admin

from minty_db.models import (
    Continent,
    CraftingIngredient,
    CraftingRecipe,
    Item,
    ItemDrop,
    Job,
    Map,
    MapleClass,
    Mob,
    MobSpawn,
    NPC,
    NPCLocation,
    NPCShopItem,
    Quest,
    QuestReward,
    Region,
    Skill,
)


@admin.register(MapleClass)
class MapleClassAdmin(admin.ModelAdmin):
    list_display = ("name", "source_id")
    search_fields = ("name",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "maple_class", "source_id")
    list_filter = ("maple_class",)
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "job", "source_id")
    list_filter = ("job",)
    search_fields = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "slot", "category", "subcategory", "source_id")
    list_filter = ("slot", "category", "subcategory")
    search_fields = ("name",)


@admin.register(Mob)
class MobAdmin(admin.ModelAdmin):
    list_display = ("name", "hp", "exp", "mesos", "source_id")
    search_fields = ("name",)


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ("name", "source_id")
    search_fields = ("name",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "continent", "source_id")
    list_filter = ("continent",)
    search_fields = ("name",)


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "source_id")
    list_filter = ("region",)
    search_fields = ("name",)


@admin.register(NPC)
class NPCAdmin(admin.ModelAdmin):
    list_display = ("name", "source_id")
    search_fields = ("name",)


@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ("name", "quest_line", "required_level", "source_id")
    list_filter = ("quest_line", "required_level")
    search_fields = ("name",)


@admin.register(CraftingRecipe)
class CraftingRecipeAdmin(admin.ModelAdmin):
    list_display = ("result_item", "result_quantity", "meso_cost", "crafter_npc")
    list_filter = ("crafter_npc",)


@admin.register(ItemDrop)
class ItemDropAdmin(admin.ModelAdmin):
    list_display = ("item", "mob", "drop_rate")
    list_filter = ("mob",)


@admin.register(MobSpawn)
class MobSpawnAdmin(admin.ModelAdmin):
    list_display = ("mob", "map")
    list_filter = ("map", "mob")


@admin.register(NPCLocation)
class NPCLocationAdmin(admin.ModelAdmin):
    list_display = ("npc", "map")
    list_filter = ("map", "npc")


@admin.register(NPCShopItem)
class NPCShopItemAdmin(admin.ModelAdmin):
    list_display = ("npc", "item", "price")
    list_filter = ("npc",)


@admin.register(QuestReward)
class QuestRewardAdmin(admin.ModelAdmin):
    list_display = ("quest", "item", "quantity", "reward_group")
    list_filter = ("quest", "reward_group")


@admin.register(CraftingIngredient)
class CraftingIngredientAdmin(admin.ModelAdmin):
    list_display = ("recipe", "item", "quantity")
    list_filter = ("recipe",)
