from django.db import models

from api.models.base import BaseModel, SoftDeleteManager, SoftDeleteQuerySet
from api.models.game.base import BaseGameDataModel


class CraftingRecipeQuerySet(SoftDeleteQuerySet):
    def with_result(self):
        return self.select_related("result_item")

    def with_ingredients(self):
        return self.prefetch_related("craftingingredient_set__item")

    def with_npc(self):
        return self.select_related("crafter_npc")

    def with_all_relations(self):
        return self.select_related("result_item", "crafter_npc").prefetch_related(
            "craftingingredient_set__item"
        )


class CraftingRecipe(BaseGameDataModel):
    """
    Represents a crafting recipe in MapleStory.
    """

    result_item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="crafted_by_recipes"
    )
    result_quantity = models.IntegerField(default=1)

    meso_cost = models.IntegerField(blank=True, null=True)

    crafter_npc = models.ForeignKey(
        "NPC",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="crafting_recipes",
    )

    objects = SoftDeleteManager.from_queryset(CraftingRecipeQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} -> {self.result_quantity}x {self.result_item.name}"


class CraftingIngredient(BaseModel):
    """
    Represents an ingredient required for a crafting recipe.
    """

    recipe = models.ForeignKey(CraftingRecipe, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = "game_crafting_ingredient"
        unique_together = [["recipe", "item"]]
        ordering = ["item__name"]

    def __str__(self):
        return f"{self.quantity}x {self.item.name} for {self.recipe.name}"
