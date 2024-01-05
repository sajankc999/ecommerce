from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def list_product(request):
    context ={
        "error":"no name was passed"
    }
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        description = data.get("description")
        category = data.get("category")
        img = request.FILES.get("img")
        if name =='':
            return render(request,"add_product.html",context)
        product_list.objects.create(
            Pname = name,
            Pprice=price,
            Pdescription=description,
            category=category,
            Pimg = img
        )
    return render(request,"add_product.html")


@api_view(['GET','POST'])
def category_list(request):
    if request.method=='GET':
        category = Category.objects.all()
        serializer = catagoryserializer(category,many=True)
        return Response(serializer.data)   
    else:
        serializer = catagoryserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "details":"new category created",
        }) 
            