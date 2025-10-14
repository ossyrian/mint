from django.db import models

from api.models.base import SoftDeleteManager, SoftDeleteQuerySet
from api.models.game.base import BaseGameDataModel


class ContinentQuerySet(SoftDeleteQuerySet):
    def with_regions(self):
        return self.prefetch_related("regions")

    def with_maps(self):
        return self.prefetch_related("regions__maps")


class Continent(BaseGameDataModel):
    """
    Represents a MapleStory continent (e.g. Victoria Island).
    """

    objects = SoftDeleteManager.from_queryset(ContinentQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class RegionQuerySet(SoftDeleteQuerySet):
    def with_continent(self):
        return self.select_related("continent")

    def with_maps(self):
        return self.select_related("continent").prefetch_related("maps")


class Region(BaseGameDataModel):
    """
    Represents a MapleStory region (e.g. Perion).
    """

    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="regions"
    )

    objects = SoftDeleteManager.from_queryset(RegionQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class MapQuerySet(SoftDeleteQuerySet):
    def with_region(self):
        return self.select_related("region__continent")

    def with_mobs(self):
        return self.select_related("region__continent").prefetch_related(
            "mobspawn_set__mob"
        )

    def with_npcs(self):
        return self.select_related("region__continent").prefetch_related(
            "npclocation_set__npc"
        )

    def with_all_entities(self):
        return self.select_related("region__continent").prefetch_related(
            "mobspawn_set__mob",
            "npclocation_set__npc",
        )


class Map(BaseGameDataModel):
    """
    Represents a MapleStory map (e.g. Land of Wild Boar).
    """

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="maps")

    objects = SoftDeleteManager.from_queryset(MapQuerySet)()

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
