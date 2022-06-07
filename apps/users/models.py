import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name=("Email Address"), unique=True)
    first_name = models.CharField(verbose_name=_('First name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=50)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+6100000000")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name","phone_number"]

    objects = CustomUserManager()
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("User")

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_email(self):
        return self.email