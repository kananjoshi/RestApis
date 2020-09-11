from products.models import Product
from rest_framework import  serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth =  2
        fields = ('id','name','price','category','image')
