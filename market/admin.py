from django.contrib import admin

from market.models import Product


class ProductAdmin(admin.ModelAdmin):

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
