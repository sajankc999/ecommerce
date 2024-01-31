from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_per_page=10
    search_fields=("name",)

@admin.register(product_list)

class product_listAdmin(admin.ModelAdmin):
    list_display=('name','price','description','category_id',)
    search_fields=('name',)
    list_per_page=10
    # autocomplete_fields=('name',)

# @admin.register(User)
# class userAdmin(admin.ModelAdmin):
#     list_display = ('username','email','password')
#     list_per_page =10
#     search_fields=('username','email')

@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display = ('address','gender','phone_number','user')
    list_per_page =10
    search_fields=('phone_number','user__email')


class orderitemInline(admin.TabularInline):
    model = orderitem
    

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ('customer',)
    list_per_page=10
@admin.register(cartItem)
class cartItemAdmin(admin.ModelAdmin):
    list_display =['cart','product','quantity']

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    list_display = ('product_list','quantity','order_status','payment_status','shipping_address')
    list_per_page=10
    inlines=(orderitemInline,)

# @admin.register(orderitem)
# class orderitemAdmin(admin.ModelAdmin):
#     list_display = ('product_list','quantity','order_status')
#     list_per_page=10
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product','customer','star')
    list_per_page=10
