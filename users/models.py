import os
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


class User(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserCustomer(User):
    class Meta:
        verbose_name = 'User Customer'
        verbose_name_plural = 'Users Customer'

    phone = models.CharField(blank=True, max_length=50)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    type = models.CharField(blank=False, max_length=15, default="customer")
    accepted_terms = models.BooleanField(blank=False, default=False)

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def get_avatar(self):
        return self.avatar

    def get_type(self):
        return self.type

    def get_is_active(self):
        return self.is_active

    def get_accepted_terms(self):
        return self.accepted_terms


class UserCompany(User):
    class Meta:
        verbose_name = 'User Company'
        verbose_name_plural = 'Users Companies'

    company_name = models.CharField(blank=True, max_length=300)
    phone = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=300)
    cif = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    type = models.CharField(blank=False, max_length=15, default="company")
    accepted_terms = models.BooleanField(blank=False, default=False)
