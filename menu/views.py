from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Fit, Food
from .serializers import FitListSerializer, FitDetailSerializer


class FitListApiView(ListAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitListSerializer


class FitDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitDetailSerializer
    lookup_field = 'id'