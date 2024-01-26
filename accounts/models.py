from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .utils import AccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    PAYMENT_PLAN=(
        ('F','Free tier'),
        ('B','Basic')
    )
    PLATFORMS=(
        ('W','WhatsApp'),
        ('D','Discord'),
        ('B','Both')
    )
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(
        max_length=255, unique=True, blank=True, null=True, verbose_name="Email"
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last login")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    location = models.CharField(max_length=20, default="Waanverse")
    payment_plan=models.CharField(max_length=1, choices=PAYMENT_PLAN, default="F")
    platform=models.CharField(max_length=1,choices=PLATFORMS, default="D")
    api_token=models.CharField(max_length=255, blank=True, null=True)
    api_key=models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    @property
    def image(self):
        if self.profile_image:
            url = self.profile_image.url
            return url
        else:
            return None

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True

