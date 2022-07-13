from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User) #method 1
def login_success(sender, request, user, **kwargs):
    print("----------------------------------")
    print("Logged-in signal")
    print("sender:", sender)
    print('rwquest:', request)
    print('user:', user)
    print(f"kwargs: {kwargs}")

    # user_logged_in.connect(login_success, sender=User) method 2


    #there are different types of inbuilt signals...these were logina nd logout//////we have model etc etc/....