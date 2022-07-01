from secrets import choice
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    CUP = 'c'
    OUNCE = 'oz'
    UNIT_CHOICES = [
        (OUNCE, 'ounce'),
        (CUP, 'cup')
    ]
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default='oz')
    quantity = models.FloatField(default=0.0)
    price_per_unit = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/ingredient"
    def __str__(self):
        return f"{self.name} {self.unit} {self.quantity} {self.price_per_unit}"


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/menu"
    def __str__(self):
        return f"{self.name} {self.price}"


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def get_absolute_url(self):
        return "/recipe"
    def __str__(self):
        return f"{self.menu_item} {self.ingredient} {self.quantity}"


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_absolute_url(self):
        return "/purchases"
    def __str__(self):
        return f"{self.user} {self.menu_item} {self.quantity}"