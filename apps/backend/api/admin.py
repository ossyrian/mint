from django.contrib import admin

from api.models import MarketplaceItem


@admin.register(MarketplaceItem)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "seller", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "description"]
