from django.contrib import admin
from products.models import Product,Category

class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id','name','price','category']
    list_search = ['id','name']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['id','name']
    list_search = ['name']

admin.site.register(Category,CategoryAdmin)
