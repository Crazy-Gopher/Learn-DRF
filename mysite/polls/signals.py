import django.dispatch

user_signup_success = django.dispatch.Signal(providing_args=['user',])

from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print("user create post_save signal")

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    print("user delete pre_delete signal")

@receiver(user_signup_success)
def user_signup(user, **kwargs):
    print("Custom signal on user creation")