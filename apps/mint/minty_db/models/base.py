from django.db import models

from common.models import BaseModel


class BaseGameDataModel(BaseModel):
    """
    Base model for all entities scraped from game data.
    Primary addition is `source_id`, which is the ID of the
    entity as represented in game files.
    """

    source_id = models.IntegerField(
        unique=True, db_index=True, default=None, blank=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self):
        return self.name
