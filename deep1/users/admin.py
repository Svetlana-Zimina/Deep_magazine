from django.contrib import admin

from carts.admin import CartTabAdmin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'phone'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone'
    ]
    inlines = [
        CartTabAdmin,
    ]
