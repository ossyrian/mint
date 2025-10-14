from django.db import models

from api.models.base import BaseModel, SoftDeleteManager, SoftDeleteQuerySet
from api.models.game.base import BaseGameDataModel
from api.models.game.world import Map


class NPCQuerySet(SoftDeleteQuerySet):
    def with_locations(self):
        return self.prefetch_related("npclocation_set__map__region__continent")

    def with_shop_items(self):
        return self.prefetch_related("npcshopitem_set__item")


class NPC(BaseGameDataModel):
    """
    Represents a MapleStory NPC.
    """

    appears_in = models.ManyToManyField(
        Map, through="NPCLocation", related_name="npc_locations"
    )
    sells = models.ManyToManyField(
        "Item", through="NPCShopItem", related_name="sold_by_npcs"
    )

    objects = SoftDeleteManager.from_queryset(NPCQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class NPCLocation(BaseModel):
    """
    Represents an NPC's location in the world.
    """

    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    class Meta:
        db_table = "game_npc_location"
        unique_together = [["npc", "map"]]

    def __str__(self):
        return f"{self.npc.name} in {self.map.name}"


class NPCShopItem(BaseModel):
    """
    Represents an item sold by an NPC with price.
    """

    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    price = models.IntegerField(help_text="Price in mesos")

    class Meta:
        db_table = "game_npc_shop_item"
        unique_together = [["npc", "item"]]
        ordering = ["price"]

    def __str__(self):
        return f"{self.item.name} sold by {self.npc.name} for {self.price:,} mesos"
