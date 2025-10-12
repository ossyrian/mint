from django.db import models

from api.models.base import BaseModel
from api.models.users import User


class Item(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
