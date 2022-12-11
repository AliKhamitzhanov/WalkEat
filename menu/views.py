from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Fit, Food, Set, Category
from .serializers import CategorySerializer, FitListSerializer, FitDetailSerializer
from rest_framework.viewsets import ModelViewSet


class CategoryFoodView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FitListView(ListCreateAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitListSerializer

class FitDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitDetailSerializer
    lookup_field = 'pk'