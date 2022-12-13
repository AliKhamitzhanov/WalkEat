from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MyOrders, CashBack
from .serializers import MyOrdersListSerializer, CashBackListSerializer


class MyOrdersApi(ListAPIView):
    queryset = MyOrders.objects.all()
    serializer_class = MyOrdersListSerializer
    lookup_field = 'id'


class CashBackApi(ListAPIView):
    queryset = CashBack.objects.all()
    serializer_class = CashBackListSerializer
    lookup_field = 'id'

