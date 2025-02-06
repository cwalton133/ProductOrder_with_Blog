from django.contrib import admin
from .models import Order, OrderItem, Product


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Number of empty items to display

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total_price')
    list_filter = ('created_at',)
    search_fields = ('id',)
    inlines = [OrderItemInline]
    ordering = ('-created_at',)


