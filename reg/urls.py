from django.urls import path, include
from reg.views import RegisterView, LoginAPIView, ProfileViewSet, ChangePasswordView, AddressView
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'address', AddressView, "address_api")

urlpatterns = [
                  path("login/", LoginAPIView.as_view(), name="login"),
                  path("register/", RegisterView.as_view(), name="register"),
                  path("profile/<int:pk>/", ProfileViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
                  path('change-password/', ChangePasswordView.as_view(), name='change-password'),

                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
                  path('', include(router.urls))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
