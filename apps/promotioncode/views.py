import datetime
import logging

from django.db.models import Count
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .exceptions import PromotionCodeNotFound
from .models import PromotionCode
from .serializers import PromotionCodeCreateSerializer, PromotionCodeSerializer

logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def submit_promotioncode_api_view(request):
    if "email" not in request.POST:
        return Response(
            {"error": "Please enter email"}, status=status.HTTP_400_BAD_REQUEST
        )

    data = request.data
    promo_code = data["promo_code"]
    try:
        promotion = PromotionCode.objects.get(promo_code=promo_code)
    except PromotionCode.DoesNotExist:
        raise PromotionCodeNotFound
    if promotion.email:
        return Response(
            {"error": "This promotion code has been used"},
            status=status.HTTP_403_FORBIDDEN,
        )

    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    has_submit_in_one_day = PromotionCode.objects.filter(
        email=data["email"], updated_at__gte=date_from
    ).count()
    if has_submit_in_one_day > 0:
        return Response(
            {"error": "One email address can only be used once per day."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "POST":
        serializers = PromotionCodeSerializer(promotion, data, many=False)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_promotion_code_api_view(request):
    user = request.user
    data = request.data
    serializers = PromotionCodeCreateSerializer(data=data)
    if serializers.is_valid():
        serializers.save()
        logger.info(
            f"promotion code {serializers.data.get('promo_code')} created by {user.email}"
        )
        return Response(serializers.data)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([permissions.IsAuthenticated])
def promotion_winner_selection_api_view(request, slug):
    try:
        promotion = PromotionCode.objects.get(promo_code=slug)
    except PromotionCode.DoesNotExist:
        raise PromotionCodeNotFound

    # check all promotion code is redeemed
    has_code_not_redeemed = PromotionCode.objects.filter(email="").count()
    if has_code_not_redeemed:
        return Response(
            {"error": "The competition is not completed yet."},
            status=status.HTTP_403_FORBIDDEN,
        )

    # check winner alread exists
    has_winner = PromotionCode.objects.filter(is_winner=True).count()
    if has_winner:
        return Response(
            {"error": "The lucky winner has been chosen."},
            status=status.HTTP_403_FORBIDDEN,
        )

    if request.method == "PUT":
        promotion.is_winner = True
        data = request.data
        serializers = PromotionCodeSerializer(promotion, data, many=False)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def all_promotion_code_api_view(request):
    if request.method == "GET":
        queryset = PromotionCode.objects.all().order_by("-is_winner")
        serializers = PromotionCodeSerializer(queryset, many=True)
        return Response(serializers.data)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def all_participants_api_view(request):
    if request.method == "GET":
        queryset = (
            PromotionCode.objects.values("email", "is_winner")
            .annotate(count=Count("email"))
            .order_by()
        )
        return Response(queryset)
