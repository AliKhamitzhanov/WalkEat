from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import CategoryFoodView, FitListView, FitDetailView
from rest_framework.routers import SimpleRouter

routers = SimpleRouter()
routers.register(r"category", CategoryFoodView)

urlpatterns = [
    path("", include(routers.urls)),
    path("main_menu/", FitListView.as_view()),
    path("detail_fit/<int:pk>/", FitDetailView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
