from products.models import Product,Category
from rest_framework import  serializers

# class ProductSerializer(serializers.ModelSerializer):
#     category_name = serializers.SerializerMethodField('get_category_name')
#
#     class Meta:
#         model = Product
#         depth =  2
#         fields = ('id','name','price','image','category_name')
#
#     def get_category_name(self, obj):
#         return obj.category.name
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name")


class ProductSerializer(serializers.ModelSerializer):
    # category_name = serializers.SerializerMethodField('get_category_name')
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        depth =  2
        fields = ('id','name','price','image','category')

    def get_category_name(self, obj):
        return obj.category.name

