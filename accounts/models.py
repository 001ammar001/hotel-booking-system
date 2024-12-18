from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()
