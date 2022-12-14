from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('cartmen/', CartList.as_view()),
    path('detailcart<int:id>/', CartList.as_view()),
    path('adressmen/', AdressesList.as_view()),
    path('detailadress<int:id>/', AdressesList.as_view()),
    path('checkoutmen/', CheckoutList.as_view()),
    path('detailcheckout<int:id>/', CheckoutList.as_view()),
    path(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)