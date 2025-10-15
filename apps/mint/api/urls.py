from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.guilds import GuildViewSet
from api.views.mogul import MarketplaceItemViewSet
from api.views.users import UserViewSet
from api.views.game import (
    ContinentViewSet,
    CraftingRecipeViewSet,
    JobViewSet,
    MapleClassViewSet,
    MapViewSet,
    MobViewSet,
    NPCViewSet,
    QuestViewSet,
    RegionViewSet,
    SkillViewSet,
    ItemViewSet,
)

router = DefaultRouter()

# All Mint users
router.register(r"users", UserViewSet, basename="user")

# MintyMogul - Marketplace
router.register(r"mogul/items", MarketplaceItemViewSet, basename="marketplace-item")

# MintyHQ - Guild registry
router.register(r"guilds", GuildViewSet, basename="guild")

# MintyDB - Game data endpoints
router.register(r"db/classes", MapleClassViewSet, basename="db-class")
router.register(r"db/jobs", JobViewSet, basename="db-job")
router.register(r"db/skills", SkillViewSet, basename="db-skill")
router.register(r"db/items", ItemViewSet, basename="db-item")
router.register(r"db/mobs", MobViewSet, basename="db-mob")
router.register(r"db/continents", ContinentViewSet, basename="db-continent")
router.register(r"db/regions", RegionViewSet, basename="db-region")
router.register(r"db/maps", MapViewSet, basename="db-map")
router.register(r"db/npcs", NPCViewSet, basename="db-npc")
router.register(r"db/quests", QuestViewSet, basename="db-quest")
router.register(r"db/recipes", CraftingRecipeViewSet, basename="db-recipe")

urlpatterns = [
    path("", include(router.urls)),
]
