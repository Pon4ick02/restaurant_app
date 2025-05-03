from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'dish', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
    search_fields = ('user__username', 'dish__name')
    ordering = ('-created_at',)
