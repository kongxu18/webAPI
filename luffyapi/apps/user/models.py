from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    继承 AbstractUser 是为了扩展自带的user表
    """
    telephone = models.CharField(max_length=11,unique=True)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
