from django.conf.urls import url
from products.rest_views import GetProductList

urlpatterns = [
    url(r'^get_product_list/$', GetProductList.as_view(),name='get_product_list'),
]
