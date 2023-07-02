import os
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserCustomer(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=50)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    type = models.CharField(blank=False, max_length=15,
                            default="customer")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserCompany(AbstractBaseUser):
    email = models.EmailField(unique=True)
    company_name = models.CharField(blank=True, max_length=300)
    phone = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=300)
    cif = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    type = models.CharField(blank=False, max_length=15,
                            default="company")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
