from django.db import models

from api.models.base import BaseModel


class GameDataModelMeta(models.base.ModelBase):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        if name != "BaseGameDataModel" and not new_class._meta.abstract:  # type: ignore[attr-defined]
            new_class._meta.db_table = f"game_{name.lower()}"  # type: ignore[attr-defined]

        return new_class


class BaseGameDataModel(BaseModel, metaclass=GameDataModelMeta):
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
