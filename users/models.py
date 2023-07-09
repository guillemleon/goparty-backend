import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        '''Create and save a user with the given email, and
        password.
        '''
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(unique=True, max_length=255, blank=False)
    phone = models.CharField(blank=True, max_length=50)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    accepted_terms = models.BooleanField(blank=False, default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserCustomer(User):
    class Meta:
        verbose_name = 'User Customer'
        verbose_name_plural = 'Users Customer'

    type = models.CharField(blank=False, max_length=15, default="customer")


class UserCompany(User):
    class Meta:
        verbose_name = 'User Company'
        verbose_name_plural = 'Users Companies'

    company_name = models.CharField(blank=True, max_length=300)
    country = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=300)
    cif = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True)
    type = models.CharField(blank=False, max_length=15, default="company")
