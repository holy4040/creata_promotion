from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.all_promotion_code_api_view, name="all-promotion-code"),
    path("all-participants/", views.all_participants_api_view, name="all-participants"),
    path("create/", views.create_promotion_code_api_view, name="promotion-code-create"),
    path("submit/", views.submit_promotioncode_api_view, name="promotion-code-submit"),
    path(
        "winner-selection/<slug:slug>",
        views.promotion_winner_selection_api_view,
        name="promotion-code-winner-selection",
    ),
]
