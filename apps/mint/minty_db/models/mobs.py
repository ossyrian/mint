from django.db import models

from common.models import BaseModel, SoftDeleteManager, SoftDeleteQuerySet
from minty_db.models.base import BaseGameDataModel
from minty_db.models.world import Map


class MobQuerySet(SoftDeleteQuerySet):
    def with_drops(self):
        return self.prefetch_related("itemdrop_set__item")

    def with_spawns(self):
        return self.prefetch_related("mobspawn_set__map__region__continent")

    def with_all_relations(self):
        return self.prefetch_related(
            "itemdrop_set__item",
            "mobspawn_set__map__region__continent",
        )


class Mob(BaseGameDataModel):
    """
    Represents a MapleStory mob.
    """

    hp = models.IntegerField()
    mp = models.IntegerField()
    exp = models.IntegerField()
    mesos = models.IntegerField()

    spawns_in = models.ManyToManyField(
        Map, through="MobSpawn", related_name="mob_spawns"
    )

    objects = SoftDeleteManager.from_queryset(MobQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["hp"]),
            models.Index(fields=["exp"]),
        ]

    def __str__(self):
        return self.name


class MobSpawn(BaseModel):
    """
    Represents a mob spawn location on a map.
    """

    mob = models.ForeignKey(Mob, on_delete=models.CASCADE)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)

    class Meta:
        unique_together = [["mob", "map"]]

    def __str__(self):
        return f"{self.mob.name} in {self.map.name}"
