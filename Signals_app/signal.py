from django.contrib.auth.signals import user_logged_in #signal
from django.contrib.auth.models import User #model sender

from django.db.models.signals import post_delete
from django.dispatch import receiver
from Auth_app.models import Contact


def login_success(request,**kwargs): #receiver function
    print("I am receiver function of login signal")
    print(request)
    print(kwargs['user'].email)

    ## write the logic to send email to the user 


user_logged_in.connect(login_success,sender=User) #connect


@receiver(post_delete, sender=Contact)
def delete_success(**kwargs):
    print("Hello I am post delete signal receiver function")
    print(kwargs)