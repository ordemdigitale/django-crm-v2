from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'phone_number',
        'paid', 'created_date', 'updated_date']
    list_filter = ['paid', 'created_date', 'updated_date']
    inlines = [OrderItemInline]