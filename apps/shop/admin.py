from django.contrib import admin
from .models import Product


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'price']