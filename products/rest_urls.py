from django.conf.urls import url
from products.rest_views import GetProductList,AddProduct

urlpatterns = [
    url(r'^get_product_list/$', GetProductList.as_view(),name='get_product_list'),
    url(r'^add_product/$', AddProduct.as_view(),name='add_product'),
]
