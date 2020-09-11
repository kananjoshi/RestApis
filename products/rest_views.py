from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView

from products.models import Product
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
