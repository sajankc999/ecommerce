from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authentication import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

user = get_user_model()
class registerserializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length =100)
    def validate_email(self,value):
        if user.objects.filter(email=value).exists():
            raise serializers.ValidationError({"error":"user with email already exists"})
        return value
    # def validate(self, attrs):
    #     if len(attrs.get("password"))<8:
    #         raise serializers.ValidationError({"error":"password must be atleast 8 characters.."})
    #     return super().validate(attrs)
    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError({"error":"password must be atleast 8 characters.."})
        return value 
     
class loginserializer(serializers.ModelSerializer):
    class Meta:
        model =user
        fields="__all__"