from django.contrib import admin
from .models import Dish

@admin.register(Dish)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
