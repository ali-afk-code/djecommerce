from django.contrib import admin
from .models import Item,Order,OrderItem,Customer

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)
# Register your models here.
