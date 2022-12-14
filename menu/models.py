from django.db import models

WEEK_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEK_CHOICES = ((i, day) for i, day in enumerate(WEEK_LIST))
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
    day = models.IntegerField(choices=WEEK_CHOICES, null=True)
    image = models.ImageField()
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    calories = models.PositiveSmallIntegerField()
    carbohydrates = models.PositiveSmallIntegerField()
    squirrels = models.FloatField()
    fats = models.FloatField()
    ingredients = models.TextField()
    fit = models.ForeignKey(Fit, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.title
