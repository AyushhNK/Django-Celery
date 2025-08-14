from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Celery import settings
from django.conf.urls.static import static
from myapp.views import UploadedImageViewSet

router = DefaultRouter()
router.register("images", UploadedImageViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
