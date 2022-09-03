from django.contrib import admin

# Register your models here.
from .models import Order, Product, Order,OrderItems
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItems)