from django.db import models

# Create your models here.

class FoodItem(models.Model):
    FOOD_CHOICES = [
        ('Taco', 'Taco'),
        ('Supreme Taco', 'Supreme Taco'),
        ('Quesadilla', 'Quesadilla'),
        ('Burrito', 'Burrito'),
        ('Nachos', 'Nachos'),
        ('Arroz con Pollo', 'Arroz con Pollo'),
    ]

    MEAT_CHOICES = [
        ('Ground Beef', 'Ground Beef'),
        ('Steak', 'Steak'),
        ('Chicken', 'Chicken'),
    ]

    name = models.CharField(max_length=100, choices=FOOD_CHOICES)
    meat = models.CharField(max_length=50, choices=MEAT_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.meat})"
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name