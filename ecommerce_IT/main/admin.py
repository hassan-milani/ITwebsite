from django.contrib import admin
from .models import *
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "c_name", "c_email", "c_phone"]
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "p_name", "p_price", "p_dec"]
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "order_final_price", "order_items", "client"]






admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
