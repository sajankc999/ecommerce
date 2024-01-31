from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Customer
User = get_user_model()
@receiver(post_save,sender=User)
def User_created(sender,instance,*args,**kwargs):
    Customer.objects.create(
        user =instance
        )
