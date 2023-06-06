from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):

  def create_user(self, email, name, password=None):
        
     if not email:
         raise ValueError('Users must have an email address.')

     email = self.normalize_email(email)
     user = self.model(email=email, name=name,)

     user.set_password(password)
     user.save(using=self._db)

     return user

  def create_superuser(self, email, name, password):

     user = self.create_user(email, name, password)

     user.is_superuser = True
     user.is_staff = True
     user.save(using=self._db)

     return user


class User(AbstractUser):
  
    username = models.CharField(max_length = 50, unique=True)
    email = models.EmailField(max_length = 100, unique=True)
    name = models.CharField(max_length=15)
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserProfileManager()


    def __str__(self):
       return "{}".format(self.email)

    


