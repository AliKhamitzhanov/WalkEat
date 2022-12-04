from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import FitListApiView, FitDetailApiView
from rest_framework.routers import SimpleRouter


urlpatterns = [
    path('main-menu/', FitListApiView.as_view()),
    path('detail-fit/<int:id>/', FitDetailApiView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)