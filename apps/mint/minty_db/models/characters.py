from django.db import models

from common.models import SoftDeleteManager, SoftDeleteQuerySet
from minty_db.models.base import BaseGameDataModel


class MapleClassQuerySet(SoftDeleteQuerySet):
    def with_jobs(self):
        return self.prefetch_related("jobs")

    def with_skills(self):
        return self.prefetch_related("jobs__skills")


class MapleClass(BaseGameDataModel):
    """
    Represents a MapleStory class (e.g. Warrior, Magician, Bowman, Thief).
    """

    objects = SoftDeleteManager.from_queryset(MapleClassQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class JobQuerySet(SoftDeleteQuerySet):
    def with_class(self):
        return self.select_related("maple_class")

    def with_skills(self):
        return self.select_related("maple_class").prefetch_related("skills")


class Job(BaseGameDataModel):
    """
    Represents a MapleStory job (e.g. Warrior->Spearman).
    """

    maple_class = models.ForeignKey(
        MapleClass, on_delete=models.CASCADE, related_name="jobs"
    )

    objects = SoftDeleteManager.from_queryset(JobQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class SkillQuerySet(SoftDeleteQuerySet):
    def with_job(self):
        return self.select_related("job__maple_class")


class Skill(BaseGameDataModel):
    """
    Represents a MapleStory skill.
    """

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="skills")

    objects = SoftDeleteManager.from_queryset(SkillQuerySet)()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name
