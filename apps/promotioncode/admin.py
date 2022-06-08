from django.contrib import admin

from .models import PromotionCode


class PromotionCodeAdmin(admin.ModelAdmin):
    list_display = [
        "promo_code",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_winner",
    ]
    list_filter = ["promo_code", "email", "first_name", "last_name"]


admin.site.register(PromotionCode, PromotionCodeAdmin)
