from django.shortcuts import render
from rest_framework.generics import ListAPIView
from cart.models import *
from .serializers import *


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    lookup_field = 'id'


class AdressesList(ListAPIView):
    queryset = Adresses.objects.all()
    serializer_class = AdressesListSerializer
    lookup_field = 'id'


class CheckoutList(ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutListSerializer
    lookup_field = 'id'
