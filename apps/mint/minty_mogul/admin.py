from django.contrib import admin

from minty_mogul.models import MarketplaceItem


@admin.register(MarketplaceItem)
class MarketplaceItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "seller", "created_at")
    list_filter = ("created_at", "price")
    search_fields = ("name", "description", "seller__username")
    ordering = ("-created_at",)
