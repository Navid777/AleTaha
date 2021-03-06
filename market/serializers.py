from rest_framework import serializers

from market.models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'title', 'description')
        read_only_fields = ('id', 'title', 'description')


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'price', 'category')
        read_only_fields = ('title', 'description', 'image', 'price', 'category')
