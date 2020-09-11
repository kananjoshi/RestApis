from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

urlpatterns += [
    path('api/v1/accounts/', include('accounts.rest_urls')),
    path('api/v1/products/', include('products.rest_urls')),
]
