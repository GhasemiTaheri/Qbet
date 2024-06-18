from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    is_superuser = models.BooleanField("superuser status",
                                       default=False,
                                       help_text="Designates that this user has all permissions without "
                                                 "explicitly assigning them.")

    username = models.CharField(verbose_name="username",
                                max_length=150,
                                unique=True,
                                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                                validators=[username_validator],
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                })

    email = models.EmailField(verbose_name="email address", blank=True)
    display_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='نام نمایشی')
    is_active = models.BooleanField(verbose_name="active",
                                    default=True,
                                    help_text="Designates whether this user should be treated as active. "
                                              "Unselect this instead of deleting accounts.")
    date_joined = models.DateTimeField(verbose_name="date joined", default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
