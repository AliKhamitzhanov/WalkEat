from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('cartmen/', MyOrdersApi.as_view()),
    path('detailcart<int:id>/', MyOrdersApi.as_view()),
    path('cartmen/', CashBackApi.as_view()),
    path('detailcart<int:id>/', CashBackApi.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)