from django.contrib import admin
from django.urls import path,include
from products.views import *
from rest_framework import routers

import products

# urlpatterns = [
#     # path('categories',category_list),
#     # path('category_detail/<pk>',category_detail),
#     path('categorylist/<pk>',CategoryList.as_view()),
#     path('productlist/<pk>',productList.as_view()),
#     path('customerlist/<pk>',customerList.as_view()),
#     path('userlist/<pk>',userList.as_view()),
#     # path('categorylist/<pk>',CategoryList.as_view()),

    
# ]
'''  the as-VIEW  function contains list of request and action'''

# urlpatterns = [
#     path('category',categoryview.as_view({         
#         'get':'list',
#         'post':'create',
#     })),
    
#     path('category',categoryview.as_view({
#         'get':'retrieve',
#         'put':'update',
#         'delete':'destroy',
#     }))    
# ]


'''using routers modules cuts the lines with ease. we dont have to specify the request types... '''

router= routers.SimpleRouter()
router.register('category',categoryview,basename='category')
router.register('product',productListview,basename='product')
router.register('customer',customerListview,basename='customer')
router.register('userList',userListview,basename='userList')
router.register('category',categoryview,basename='category')

urlpatterns = [
    
]+router.urls
