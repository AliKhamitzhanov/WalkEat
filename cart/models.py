from django.db import models
from menu.models import Food
from django.core.validators import MaxLengthValidator, MinLengthValidator
# Create your models here.



class Cart(models.Model):
    cart = models.ForeignKey(Food, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()
    image = models.ImageField()
    price = models.PositiveIntegerField()
    allergy = models.TextField(max_length=255)
    cutlery = models.BooleanField(default=False)

class Adresses(models.Model):
    street = models.CharField(max_length=155)
    home = models.IntegerField()
    flat = models.IntegerField()
    floor = models.IntegerField()


class Checkout(models.Model):
    name = models.CharField(max_length=55)
    number = models.IntegerField()
    note = models.CharField(max_length=100)
    adress = models.OneToOneField(Adresses, on_delete=models.CASCADE)
