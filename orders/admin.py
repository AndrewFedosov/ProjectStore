from django.contrib import admin
from .models import *

class StatusAdmin (admin.ModelAdmin):
     list_display = [field.name for field in Status._meta.fields]

     class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)


class Product_in_orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product_in_order._meta.fields]

    class Meta:
        model = Product_in_order


admin.site.register(Product_in_order, Product_in_orderAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)