from django.contrib import admin

from minty_hq.models import Guild, GuildFame, GuildTag


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")
    ordering = ("-created_at",)


@admin.register(GuildFame)
class GuildFameAdmin(admin.ModelAdmin):
    list_display = ("guild", "user", "value", "created_at")
    list_filter = ("value", "created_at")
    search_fields = ("guild__name", "user__username")
    ordering = ("-created_at",)


@admin.register(GuildTag)
class GuildTagAdmin(admin.ModelAdmin):
    list_display = ("guild", "user", "value", "created_at")
    list_filter = ("value", "created_at")
    search_fields = ("guild__name", "user__username")
    ordering = ("-created_at",)
