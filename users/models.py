from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True )
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]
    
    def __str__(self):
        return self.email
    
    
class ConfirmCode(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=6)