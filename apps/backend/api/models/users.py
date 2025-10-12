from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models.base import BaseModel


class User(AbstractUser, BaseModel):
    guild = models.ForeignKey(
        "Guild",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members",
    )

    def __str__(self):
        return self.username
