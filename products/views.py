from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics,mixins


# class based view
# from rest_framework.views import APIView
# from django.http import Http404

# class CategoryList(APIView):
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#             category = self.get_object(pk)
#             serializer = catagoryserializer(category)
#             return Response(serializer.data)

#     def put(self, request, pk, format=None):
#             snippet = self.get_object(pk)
#             serializer = catagoryserializer(snippet, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#             snippet = self.get_object(pk)
#             snippet.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)  

class CategoryList(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=catagoryserializer

class productList(generics.RetrieveUpdateDestroyAPIView):
    queryset=product_list.objects.all()
    serializer_class=productlistserializer

class customerList(generics.RetrieveUpdateDestroyAPIView):
    queryset=customer.objects.all()
    serializer_class=customerserializer

class userList(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=Userserializer

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


# @api_view(['GET','POST'])
# def category_list(request):
#     if request.method=='GET':
#         category = Category.objects.all()
#         serializer = catagoryserializer(category,many=True)
#         return Response(serializer.data)   
#     else:
#         serializer = catagoryserializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({
#             "details":"new category created",
#         }) 
# @api_view(['GET','DELETE','PUT'])
# def category_detail(request,pk):
#     category=Category.objects.get(pk=pk)

#     if request.method =="GET":
#         serailizer = catagoryserializer(category)
#         return Response(serailizer.data)
#     if request.method =='DELETE':
#         category.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT,
#         )
#     if request.method =='PUT':
#         serailizer=catagoryserializer(category,data = request.data)
#         serailizer.is_valid(raise_exception=True)
#         serailizer.save()
#         return Response({
#             'details':'category updated'
#         })




