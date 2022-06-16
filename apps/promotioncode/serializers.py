from rest_framework import serializers

from .models import PromotionCode


class PromotionCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCode
        fields = ["id", "promo_code","email", "first_name", "last_name", "phone_number", "is_winner"]


class PromotionCodeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCode
        exclude = ["updated_at", "pkid"]
