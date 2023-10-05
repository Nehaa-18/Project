from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=20)  # Add any additional fields you need


    
    def __str__(self):
       return self.email
