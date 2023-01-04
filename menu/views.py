from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Fit
from .serializers import FitListSerializer, FitDetailSerializer


class FitListView(ListAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitListSerializer


class FitDetailView(RetrieveAPIView):
    queryset = Fit.objects.all()
    serializer_class = FitDetailSerializer
    lookup_field = 'pk'
