from django.db import models

from common.models import BaseModel, SoftDeleteManager, SoftDeleteQuerySet
from minty_db.models.base import BaseGameDataModel


class ItemQuerySet(SoftDeleteQuerySet):
    def with_drops(self):
        return self.prefetch_related("itemdrop_set__mob")


class Item(BaseGameDataModel):
    """
    Represents a MapleStory item.
    """

    class Slot(models.TextChoices):
        EQUIP = "equip", "Equipment"
        USE = "use", "Consumable"
        SETUP = "setup", "Setup"
        ETC = "etc", "Etc"
        CASH = "cash", "Cash"

    class Category(models.TextChoices):
        WEAPON = "weapon", "Weapon"
        ARMOR = "armor", "Armor"
        ACCESSORY = "accessory", "Accessory"
        CONSUMABLE = "consumable", "Consumable"
        AMMO = "ammo", "Ammo"
        SCROLL = "scroll", "Scroll"
        QUEST = "quest", "Quest Item"
        MISC = "misc", "Miscellaneous"

    slot = models.CharField(max_length=20, choices=Slot.choices, blank=True, default="")
    category = models.CharField(
        max_length=20, choices=Category.choices, blank=True, default=""
    )
    subcategory = models.CharField(max_length=50, blank=True, default="")

    # Extended attributes discovered during scraping (stack_size, reserve, etc.)
    attributes = models.JSONField(blank=True, null=True)

    dropped_by = models.ManyToManyField(
        "minty_db.Mob", through="ItemDrop", related_name="item_drops"
    )

    objects = SoftDeleteManager.from_queryset(ItemQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["slot", "category"]),
        ]

    def __str__(self):
        return self.name


class ItemDrop(BaseModel):
    """
    Represents an item drop from a mob with drop rate.
    """

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    mob = models.ForeignKey("Mob", on_delete=models.CASCADE)
    drop_rate = models.FloatField(help_text="Drop rate as a decimal (0.0 to 1.0)")

    class Meta:
        unique_together = [["item", "mob"]]
        ordering = ["-drop_rate"]
        indexes = [
            models.Index(fields=["drop_rate"]),
        ]

    def __str__(self):
        return f"{self.item.name} from {self.mob.name} ({self.drop_rate:.2%})"
