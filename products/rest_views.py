from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers

from products.models import Product, Category
from products.serializers import ProductSerializer


class GetProductList(APIView):
    """
    returns list of products
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        data = {}
        try:
            product_list = Product.objects.all().first()
            products = ProductSerializer(product_list).data
            data.update({'products': products})
            response = {
                "status": status.HTTP_200_OK,
                "message": "Successfully fetched Product List.",
                "data": data
            }

        except Product.DoesNotExist as exception:
            response = {
                "status": 404,
                "message": "Something wrong happened",
                "data": {}
            }
        return Response(response)


class AddProduct(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    """
    stores the products 
    """
    def post(self,request):
        data = {}

        try:
            datadict = request.POST.dict()
            image = request.FILES['image']
            # import pdb;pdb.set_trace()
            cat_name = datadict['category_name']
            category =  Category.objects.create(name = cat_name)
            datadict.pop('category_name')
            datadict.update({'category':category,'image':image})

            product, created = Product.objects.get_or_create(**datadict)
            print("{} {} ".format(category,product))
            resp_status = status.HTTP_201_CREATED

        except Exception as e:
            resp_status = status.HTTP_400_BAD_REQUEST
        return Response({
            'status':resp_status,
            'data' : data
        })

