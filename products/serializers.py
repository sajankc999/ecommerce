from rest_framework import serializers
from .models import *
from rest_framework import viewsets

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
    
    

# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields = ['email','username',]
class customerserializer(serializers.ModelSerializer):
    
    class Meta:
        model=Customer
        fields="__all__"
class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = product_list.objects.all(),
        source ='product'
    )
    product = productlistserializer(read_only=True)
    # customer = customerserializer(many=True)
    class Meta:
        model = cartItem
        fields=['product_id','product','quantity']
    def create(self, validated_data):
        request = self.context['request']
        # raise Exception(request.user)
        cart= Cart.objects.get(customer__user=request.user)
        cart_item = cartItem.objects.filter(cart=cart)
        # raise Exception(cart_item)

        validated_data.update(
            {
                'cart':cart,
            }
        )
        return super().create(validated_data)

    # def validate_many_values(self,attrs):
    #     if attrs['product']==cartItem.product:
    #        attrs['quantity']+=1
    #     return attrs


class CartSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    customer_id = serializers.PrimaryKeyRelatedField(
        queryset = Customer.objects.all(),
        source = "customer"
    )
    cart_items= CartItemSerializer(many=True,read_only =True,source='items') #source was introduced for reducing indirect dependency
    # raise Exception(cart_items)
    class Meta:
        model = Cart
        fields =['customer_id','customer','cart_items']





class Orderserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = order
        fields =['user','id','shipping_address']
    
    def create(self,validated_data):
        cart_items = cartItem.objects.filter(cart__cusomter__user = validated_data.get('user') )
        raise Exception(cart_items)
        order_obj = order.objects.create(
            cusomter = Customer.objects.filter(user = validated_data.get('user')),
            shipping_address  = validated_data.get('shipping_address')
                )
        order_items_obj = [
            orderitem(
                product_list=items.product,
                quantity = items.quantity,
                price = items.product.price,
                order = order_obj,

            ) 
            for items in cart_items]

class orderitemserializer(serializers.ModelSerializer):
    class Meta:
        model = orderitem
        fields = "__all__"

class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"