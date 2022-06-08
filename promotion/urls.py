from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("creata_portal/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/promotioncode/", include("apps.promotioncode.urls")),
]

admin.site.site_header = "Creata Project"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Portal"
