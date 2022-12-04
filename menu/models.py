from django.db import models

WEEK_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
WEEK_CHOICES = ((day, day) for day in WEEK_LIST)
CATEGORY_LIST = ["breakfast", "lunch", "snack", "dinner"]
CATEGORY_CHOICES = ((category, category) for category in CATEGORY_LIST)

class Fit(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    kcal = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.title


class Food(models.Model):
    title = models.CharField(max_length=255, unique=True)
    calories = models.PositiveSmallIntegerField()
    squirrels = models.FloatField()
    carbohydrates = models.PositiveSmallIntegerField()
    fats = models.FloatField()
    ingredients = models.TextField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, null=True)
    fit = models.ForeignKey(Fit, on_delete=models.PROTECT, null=True, related_name="food")
    day = models.CharField(max_length=255, choices=WEEK_CHOICES, null=True)

    def __str__(self) -> str:
        return self.title
