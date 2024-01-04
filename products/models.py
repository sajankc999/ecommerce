from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class product_list(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.name


class User(models.Model):
    username=models.CharField(max_length=55)
    email= models.CharField(max_length = 100)
    password = models.CharField( max_length=100)
    def __str__(self):
        return self.username

class customer(models.Model):
    address =models.IntegerField()
    gender = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    def __str__(self):
        return self.user

class Cart(models.Model):
    customer = models.ForeignKey(customer,on_delete = models.CASCADE)

       

class order(models.Model):
    product_list = models.ForeignKey(product_list,on_delete=models.CASCADE,default="")
    quantity = models.IntegerField(default = 1)
    confrim ="c"
    pending = "p"
    confirm ="C"
    status_choices = [
        ("c","confirm"),
        ("P",'pending'),
        ("C","completed")
    ]
    order_status = models.CharField(max_length=1,default = pending, choices = status_choices)
    payment_status = models.BooleanField(default = False)
    shipping_address = models.CharField(max_length = 200)
    def __str__(self):
        return self.order_status

class orderitem(models.Model):
    product_list = models.ForeignKey(product_list,on_delete=models.CASCADE,default="")
    quantity = models.IntegerField(default = 1)   
    confrim ="c"
    pending = "p"
    confirm ="C"
    status_choices = [
        (confirm,"confirm"),
        (pending,'pending'),
        (confirm,"ccompleted")
    ]
    order_status = models.CharField(max_length=1,default = pending, choices = status_choices) 
    order_id = models.ForeignKey(order,on_delete=models.CASCADE)
    def __str__(self):
        return self.order_status

class Review(models.Model):
    product = models.ForeignKey(product_list,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete =models.CASCADE)
    star = models.IntegerField()
    def __str__(self):
        return self.star



