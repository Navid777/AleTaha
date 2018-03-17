from django.contrib import admin

from market.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')

    class Meta:
        model = Product


class ProductCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = ProductCategory

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
