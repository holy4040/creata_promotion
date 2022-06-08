import random
import string

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class PromotionCode(TimeStampedUUIDModel):
    promo_code = models.CharField(
        verbose_name=_("Promotion Code"), max_length=255, unique=True
    )
    email = models.EmailField(verbose_name=("Email Address"), blank=True, null=True)
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=50, blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=50, blank=True, null=True
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=30, blank=True, null=True
    )
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return self.promo_code

    class Meta:
        verbose_name = "Promotion Code"
        verbose_name_plural = "Promotion Code"

    def save(self, *args, **kwargs):
        super(PromotionCode, self).save(*args, **kwargs)
