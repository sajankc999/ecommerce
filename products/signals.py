from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()
@receiver(post_save,sender=User)
def User_created(sender,instance,*args,**kwargs):
    print("user created!!")