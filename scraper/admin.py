from django.contrib import admin
from .models import ScrapedItem, ScrapingLog

@admin.register(ScrapedItem)
class ScrapedItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'source', 'scraped_at', 'is_active']
    list_filter = ['category', 'source', 'is_active']
    search_fields = ['title', 'description']
    readonly_fields = ['scraped_at', 'updated_at', 'times_viewed']

@admin.register(ScrapingLog)
class ScrapingLogAdmin(admin.ModelAdmin):
    list_display = ['source', 'items_found', 'items_new', 'success', 'started_at']
    list_filter = ['success', 'source']
