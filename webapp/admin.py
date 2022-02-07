from django.contrib import admin

from webapp.models import Product, Client, Order, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'price']
    list_filter = ['category']
    search_fields = ['category', 'price']
    fields = ['title', 'description', 'category', 'balance', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Cart)
