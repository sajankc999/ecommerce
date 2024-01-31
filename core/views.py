from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token  
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import * 
from django.contrib.auth import get_user_model


from django.conf import settings
from django.core.mail import send_mail
userobj = get_user_model()#extracting custom User model from core.models
# Create your views here.
'''login and register with class view'''

# class registerViewset(viewsets.ModelViewSet):
#     queryset= user.objects.all()
#     serializer_class= registerserializer 
#     def create(self,request):  
#         username = request.data.get('username')
#         password = request.data.get('password')
        

#         if User.objects.filter(username=username).exists():
#             return Response({"message":"user exists"})
#         else:
#             user=user.objects.create_user(username=username,password=password)
#             token ,_ = Token.objects.get_or_create(user=user)
#             return Response({
#                 "status":"created",
#                 "username":user.get_username(),
#                 "token":token.key,
#             })
# class loginViewset(viewsets.ModelViewSet):
#     queryset=user.objects.filter()
#     serializer_class=loginserializer

#     # @action(methods=['POST'],detail=True)
#     def retrieve(self,request):
#         username=request.data.get("username")
#         password=request.data.get("password")
#         # serializer = loginserializer(data = request.data)
#         # if not serializer.is_valid():
#         #     return Response("invalid datails")
#         # serializer.save()
#         user = authenticate(username=username,password = password)
#         if user:
#             token,_=Token.objects.get_or_create(user=user)
#             return Response({
#                 "details":user.get_username,
#                 "token":token.key,                    
#             })
#         return Response("user dosent exists")



# class loginViewset(APIView):
#     def post(self,request):
#         try:
#             username=request.data.username
#             password=request.data.password
#             serializer = loginserializer(data = request.data)
#             if not serializer.is_valid():
#                 return Response({
#                     "message":serializer.errors,
#                     })
#             serializer.save()
#             user = authenticate(username=username,password = password)
#             if user:
#                 token,_=Token.objects.get_or_create(user=user)
#                 return Response({
#                     "username":user.get_username(),
#                     "token":token.key,                    
#                 })
#         except Exception as e:
#             return Response({"error":e,})


'''login and register with function view'''
@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(username = email,password=password)
    if user:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({
            "username":user.get_username(),
            "token":token.key,
        })
    return  Response(user)



@api_view(['POST'])
def register(request):
    serializer = registerserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    password = serializer.validated_data.get('password')
    

    if userobj.objects.filter(email=email).exists():
        return Response({"message":"user exists"})
    else:
        user=userobj.objects.create_user(email=email,password=password)
        if user:
            send_mail(
                "verification link . PLEAE DONOT SHARE",
                "hello",
                "ecommerce@gmail.com",
                [user.email],
            )
            return Response({
            "status":"created",
            })


