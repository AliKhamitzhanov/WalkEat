# from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import CardSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Card


class CardView(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    # lookup_field = 'pk'
