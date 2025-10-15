from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import BaseModel


class User(AbstractUser, BaseModel):
    guild = models.ForeignKey(
        "minty_hq.Guild",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="members",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.username
