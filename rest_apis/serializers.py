from rest_framework import serializers
from .models import *
# https://wsvincent.com/django-rest-framework-authentication-tutorial/#:~:text=authtoken%20which%20is%20Django%20Rest,api%2Furls.py%20file.&text=We%20have%20a%20working%20login,rest%2Dauth%2Flogout%2F.

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'category',
            'image'
        )
        model = Product
