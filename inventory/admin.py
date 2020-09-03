from django.contrib import admin
from .models import Product, Discount, ProductGroup


admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(ProductGroup)
