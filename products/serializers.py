from rest_framework import serializers
from .models import *

# class catagoryserializer(serializers.Serializer):
#     id =serializers.IntegerField()
#     name = serializers.CharField()

'''to implement this way we need to define each functions manually'''

    # def create(self,validated_data):
    #     instance = Category.objects.create(**validated_data)
    #     return instance


class catagoryserializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['id','name'] # "__all__ for all data"
class productlistserializer(serializers.ModelSerializer):
    class Meta:
        model=product_list
        fields ="__all__"

class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field = ['email','username',]
class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = "__all__"

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model = order
        field = "__all__"

class orderitemserializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem
        field = "__all__"

class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = "__all__"