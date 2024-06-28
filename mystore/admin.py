from django.contrib import admin
from .product import Product
from .category import Category
# Register your models here.

class Categoryinfo(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Product)
admin.site.register(Category, Categoryinfo)