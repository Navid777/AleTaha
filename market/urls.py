from django.conf.urls import url
from market.views import ProductList, ProductCategoryList

urlpatterns = [
    url('product_list/$', ProductList.as_view()),
    url('category_list/$', ProductCategoryList.as_view()),
]