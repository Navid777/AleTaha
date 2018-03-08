from rest_framework import generics

from market.models import ProductCategory, Product
from market.serializers import ProductCategorySerializer, ProductSerializer


class ProductCategoryList(generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
