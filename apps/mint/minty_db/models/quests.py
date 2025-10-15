from django.db import models

from common.models import BaseModel, SoftDeleteManager, SoftDeleteQuerySet
from minty_db.models.base import BaseGameDataModel


class QuestQuerySet(SoftDeleteQuerySet):
    def with_npc(self):
        return self.select_related("started_by")

    def with_rewards(self):
        return self.prefetch_related("questreward_set__item")

    def with_requirements(self):
        return self.select_related(
            "prerequisite_quest", "required_class", "required_job"
        )

    def with_all_relations(self):
        return self.select_related(
            "started_by", "prerequisite_quest", "required_class", "required_job"
        ).prefetch_related("questreward_set__item")


class Quest(BaseGameDataModel):
    """
    Represents a MapleStory quest.
    """

    started_by = models.ForeignKey(
        "NPC", on_delete=models.CASCADE, related_name="quests"
    )

    quest_line = models.CharField(max_length=200, blank=True, default="")

    meso_reward = models.IntegerField(blank=True, null=True)
    exp_reward = models.IntegerField(blank=True, null=True)

    prerequisite_quest = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="unlocks_quests",
    )

    required_level = models.IntegerField(blank=True, null=True)
    required_class = models.ForeignKey(
        "MapleClass",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="class_quests",
    )
    required_job = models.ForeignKey(
        "Job",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="job_quests",
    )

    misc_requirements = models.JSONField(blank=True, null=True)

    objects = SoftDeleteManager.from_queryset(QuestQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["quest_line"]),
            models.Index(fields=["required_level"]),
        ]

    def __str__(self):
        return self.name


class QuestReward(BaseModel):
    """
    Represents an item reward for completing a quest.

    reward_group semantics:
    - 0: Guaranteed rewards (player receives all)
    - 1+: Choice pools (player picks one from each group)
    """

    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    reward_group = models.IntegerField(default=0)

    class Meta:
        unique_together = [["quest", "item"]]
        ordering = ["reward_group", "item__name"]

    def __str__(self):
        group_type = (
            "guaranteed"
            if self.reward_group == 0
            else f"choice group {self.reward_group}"
        )
        return (
            f"{self.quantity}x {self.item.name} from {self.quest.name} ({group_type})"
        )
