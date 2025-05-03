from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'is_seller', 'is_active', 'is_staff')
    search_fields = ('phone_number', 'username')  # Добавим возможность поиска по номеру телефона
    list_filter = ('is_seller',)  # Фильтрация по роли продавца
    list_editable = ('is_seller',)  # Сделаем поле для редактирования роли продавца прямо в списке

admin.site.register(User, UserAdmin)
