
from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_last_name",
        "phone",
        "delivery_type",
        "pickup_place",
        "status",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "user_last_name",
        "user_first_name",
        "id",
        "delivery_type"
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "user_first_name",
        "user_last_name",
        "requires_delivery",
        "status",
        "is_paid",
    )
    inlines = (OrderItemTabulareAdmin,)
