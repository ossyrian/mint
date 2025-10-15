from django.db import models

from common.models import BaseModel, SoftDeleteManager, SoftDeleteQuerySet


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


class CraftingRecipe(BaseModel):
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
        ordering = ["result_item__name"]
        indexes = [
            models.Index(fields=["result_item", "crafter_npc"]),
            models.Index(fields=["meso_cost"]),
        ]

    def __str__(self):
        return f"{self.result_item.name} recipe ({self.uuid})"


class CraftingIngredient(BaseModel):
    """
    Represents an ingredient required for a crafting recipe.
    """

    recipe = models.ForeignKey(CraftingRecipe, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = [["recipe", "item"]]
        ordering = ["item__name"]

    def __str__(self):
        return f"{self.quantity}x {self.item.name} for {self.recipe}"
