from django.contrib import admin
from django.urls import path,include
from products.views import *

import products
urlpatterns = [
    # path('categories',category_list),
    # path('category_detail/<pk>',category_detail),
    path('categorylist/<pk>',CategoryList.as_view()),
    path('productlist/<pk>',productList.as_view()),
    path('customerlist/<pk>',customerList.as_view()),
    path('userlist/<pk>',userList.as_view()),
    # path('categorylist/<pk>',CategoryList.as_view()),

    
]