import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    """Manager that excludes soft-deleted records by default."""

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

    def all_with_deleted(self):
        """Return all records including soft-deleted ones."""
        return super().get_queryset()

    def deleted_only(self):
        """Return only soft-deleted records."""
        return super().get_queryset().filter(deleted_at__isnull=False)


class BaseModel(models.Model):
    """Abstract base model with UUID, soft deletion, and timestamps."""

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Access all records including deleted

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """Soft delete by setting deleted_at timestamp."""
        self.deleted_at = timezone.now()
        self.save(using=using)

    def hard_delete(self, using=None, keep_parents=False):
        """Permanently delete the record from database."""
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        """Restore a soft-deleted record."""
        self.deleted_at = None
        self.save()


class User(AbstractUser, BaseModel):
    """Custom User model with UUID for public identification."""

    guild = models.ForeignKey(
        'Guild',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members',
    )

    def __str__(self):
        return self.username


class Guild(BaseModel):
    """Guild model for MintyHQ guild registry."""

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_guilds',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Item(BaseModel):
    """Example model for a marketplace item."""

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
