from django.contrib import admin
from django.urls import path,include
from products.views import *

import products
urlpatterns = [
    path('categories',category_list)

    
]