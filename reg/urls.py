from django.urls import path, include
from reg.views import RegisterView, LoginAPIView, ProfileViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings


router = DefaultRouter()
router.register(r'profile', ProfileViewSet, "profile_api")

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)