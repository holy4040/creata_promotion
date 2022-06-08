from apps.promotioncode.models import PromotionCode
from apps.promotioncode.serializers import (PromotionCodeCreateSerializer,
                                            PromotionCodeSerializer)


def run():
    code_list = ["ZVLJCYTG", "AC4ICZFM", "2PKFJHPY", "GF2GY8ZF", "XH4Z5946"]
    for c in code_list:
        PromotionCode.objects.create(promo_code=c)
