from django.urls import path, include
from .views import CardView
from rest_framework.routers import DefaultRouter

card = DefaultRouter()
card.register(r"card", CardView, 'api_card')

urlpatterns = [
    # path('card/', CardView.as_view({'get': 'retrieve', 'post': 'create'}), name="card"),
    path('', include(card.urls))

]
