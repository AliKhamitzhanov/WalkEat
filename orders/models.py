from django.db import models
from cart.models import Cart


class MyOrders(models.Model):
    date = models.DateField()
    image = models.ImageField()
    count = models.IntegerField()
    title = models.CharField(max_length=155)
    price = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class CashBack(models.Model):
    cashback = models.TextField(max_length=255)
