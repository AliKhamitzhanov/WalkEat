from django.db import models

WEEK_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEK_CHOICES = ((day, day) for day in WEEK_LIST)
CATEGORY_LIST = ["breakfast", "lunch", "snack", "dinner"]
CATEGORY_CHOICES = ((category, category) for category in CATEGORY_LIST)



class Category(models.Model):
    category_name = models.CharField(max_length=255, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self) -> str:
        return self.category_name

class Fit(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20)
    description = models.TextField()
    kcal = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    def __str__(self) -> str:
        return self.title

class Food(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    calories = models.PositiveSmallIntegerField()
    carbohydrates = models.PositiveSmallIntegerField()
    squirrels = models.FloatField()
    fats = models.FloatField()
    ingredients = models.TextField()
    
    def __str__(self) -> str:
        return self.title

foods_choice = [(food.id, food.title) for food in Food.objects.all()]

class Set(models.Model):
    day = models.CharField(max_length=255, choices=WEEK_CHOICES)
    breakfast = models.IntegerField(choices=foods_choice, null=True)
    lunch = models.IntegerField(choices=foods_choice, null=True)
    snack = models.IntegerField(choices=foods_choice, null=True)
    dinner = models.IntegerField(choices=foods_choice, null=True)
    fit = models.ForeignKey(Fit, on_delete=models.PROTECT)

