from django.db import models
from django.core.validators import MinValueValidator
from users.models import User
from posts.models import Post

# Create your models here.
class MealProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='meal_provider')
    location = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0)])
    review_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"Meal Provider: {self.user.email}"  

class Meal(models.Model):
    MEAL_TYPE_CHOICES = [
        ('BREAKFAST', 'Breakfast'),
        ('LUNCH', 'Lunch'),
        ('DINNER', 'Dinner'),
        ('SNACK', 'Snacks/Starters'),
        ('DESSERT', 'Dessert'),
    ]

    provider = models.ForeignKey(MealProvider, on_delete=models.CASCADE, related_name='meals')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='meals')
    name = models.CharField(max_length=200, default='Unnamed Meal')
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"{self.name} ({self.get_meal_type_display()})"