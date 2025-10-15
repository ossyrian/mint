from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models, transaction
from django.db.models import Count, Sum
from simple_history.models import HistoricalRecords

from common.models import BaseModel

if TYPE_CHECKING:
    from django.db.models.fields.related_descriptors import RelatedManager
    from users.models import User


class Guild(BaseModel):
    """
    Guilds have owners and members. Owners are 1:1, while
    members are 1:n.
    """

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owned_guilds",
    )

    if TYPE_CHECKING:
        fame: RelatedManager[GuildFame]
        tags: RelatedManager[GuildTag]

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @transaction.atomic
    def set_fame(self, user: User, value: GuildFame.FameValue):
        """
        Add or update a user's fame rating for this guild.
        """
        fame, _ = self.fame.update_or_create(
            user=user,
            defaults={"value": value},
        )
        return fame

    @transaction.atomic
    def remove_fame(self, user: User):
        """
        Remove a user's fame rating for this guild.
        """
        deleted_count, _ = self.fame.filter(user=user).delete()
        return deleted_count

    def get_total_fame(self):
        """
        Calculate the total fame for this guild.
        """
        result = self.fame.aggregate(total=Sum("value"))
        return result["total"] or 0

    def get_fame_count(self):
        """
        Get counts of fame and defame ratings.
        """
        fame_count = self.fame.filter(value=1).count()
        defame_count = self.fame.filter(value=-1).count()
        return {"fame": fame_count, "defame": defame_count}

    @transaction.atomic
    def add_tag(self, user: User, tag_value: GuildTag.TagValue):
        """
        Add a tag to this guild from a user. Users can assign
        up to 5 unique tags to a guild at any given time.

        Raises:
            ValueError: If user already has 5 tags for this guild
        """
        existing_tag = self.tags.filter(user=user, value=tag_value).first()
        if existing_tag:
            return existing_tag, False

        user_tag_count = self.tags.filter(user=user).count()
        if user_tag_count >= 5:
            raise ValueError(
                f"User {user.username} has already assigned 5 tags to this guild."
                "Remove a tag before adding a new one."
            )

        tag = self.tags.create(user=user, value=tag_value)
        return tag

    @transaction.atomic
    def remove_tag(self, user: User, tag_value: GuildTag.TagValue):
        """
        Remove a specific tag from a user for this guild.
        """
        deleted_count, _ = self.tags.filter(user=user, value=tag_value).delete()
        return deleted_count

    def get_tag_counts(self):
        """
        Get counts of each tag type for this guild.
        """
        tag_counts = (
            self.tags.values("value").annotate(count=Count("id")).order_by("-count")
        )

        return {item["value"]: item["count"] for item in tag_counts}

    def get_user_tags(self, user: User):
        """
        Get all tags a specific user has given to this guild.
        """
        return self.tags.filter(user=user)

    def get_fame_history(self, user: User | None = None):
        """
        Get historical fame events for this guild.
        """
        HistoricalGuildFame = self.fame.model.history.model
        queryset = HistoricalGuildFame.objects.filter(guild=self)

        if user is not None:
            queryset = queryset.filter(user=user)

        return queryset.order_by("-history_date")

    def get_tag_history(self, user: User | None = None):
        """
        Get historical tag events for this guild.
        """
        HistoricalGuildTag = self.tags.model.history.model
        queryset = HistoricalGuildTag.objects.filter(guild=self)

        if user is not None:
            queryset = queryset.filter(user=user)

        return queryset.order_by("-history_date")


class GuildFame(BaseModel):
    """
    Model for tracking guild fame. Users are able to give a persistent
    "fame/defame" rating to guilds. Persisted as a separate
    table in order to allow fame/defame givers and their properties
    to be queried.
    """

    class FameValue(models.IntegerChoices):
        DEFAME = -1, "Defame"
        FAME = 1, "Fame"

    guild = models.ForeignKey(
        Guild,
        on_delete=models.CASCADE,
        related_name="fame",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="guild_fame_given",
    )
    value = models.IntegerField(choices=FameValue.choices)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["guild", "user"]

    def __str__(self):
        return f"{self.user.username} -> {self.guild.name}: {self.get_value_display()}"  # type: ignore


class GuildTag(BaseModel):
    """
    Model for tracking guild tags. Users are able to award persistent
    tags to guilds. Persisted as a separate table in order to allow bestowers
    and their properties to be queried.

    Users can assign multiple tags to a guild, but each specific tag only once.
    """

    class TagValue(models.TextChoices):
        BOSSERS = "bossers", "Bossers"
        CASUALS = "casuals", "Casuals"
        DEAD_GUILD = "dead_guild", "Dead Guild"
        DRAMA = "drama", "Drama"
        F2P_PRIDE = "f2p_pride", "F2P Pride"
        FASHIONSTORY = "fashion_story", "FashionStory"
        HELPFUL = "helpful", "Helpful"
        MOGULS = "moguls", "Moguls"
        NO_LIFERS = "no_lifers", "No-Lifers"
        NOOB_FRIENDLY = "noob_friendly", "Noob Friendly"
        PQ_ENJOYERS = "pq_enjoyers", "PQ Enjoyers"
        SOCIAL = "social", "Social"
        UNCS = "uncs", "Uncs"
        WEEBS = "weebs", "Weebs"
        WHOLESOME = "wholesome", "Wholesome"

    guild = models.ForeignKey(
        Guild,
        on_delete=models.CASCADE,
        related_name="tags",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="guild_tags_given",
    )
    value = models.CharField(max_length=50, choices=TagValue.choices)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["guild", "user", "value"]

    def __str__(self):
        return f"{self.user.username} -> {self.guild.name}: {self.get_value_display()}"  # type: ignore
