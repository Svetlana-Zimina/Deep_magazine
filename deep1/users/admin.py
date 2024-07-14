from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки модели Пользователь
    для отображения в панели администратора."""

    list_display = [
        'username',
        'email',
        'phone'
    ]
    search_fields = [
        'username',
        'email',
        'phone'
    ]
