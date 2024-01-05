from rest_framework import serializers
from .models import *

# class catagoryserializer(serializers.Serializer):
#     id =serializers.IntegerField()
#     name = serializers.CharField()


class catagoryserializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields =['id','name'] # "__all__ for all data"