from rest_framework import serializers
from .models import *

# class catagoryserializer(serializers.Serializer):
#     id =serializers.IntegerField()
#     name = serializers.CharField()

'''to implement this way we need to define each functions manually'''

    # def create(self,validated_data):
    #     instance = Category.objects.create(**validated_data)
    #     return instance


class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['id','name'] # "__all__ for all data"


class productlistserializer(serializers.ModelSerializer):
    category = categoryserializer(read_only =True)
    price_with_tax = serializers.SerializerMethodField()
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source ='category',
    )
    class Meta:

        model=product_list
        fields =('name','price','description','price_with_tax','category','category_id',)


    def get_price_with_tax(self,product):
        return (float(product.price) * 0.13) + float(product.price)
    
    
class customerserializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['email','username',]
class cartserializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class orderserializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = "__all__"

class orderitemserializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem
        fields = "__all__"

class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"