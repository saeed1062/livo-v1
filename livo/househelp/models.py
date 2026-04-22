from django.db import models
from users.models import User

# Create your models here.

class SkillTag(models.Model):
    """The 'Master List' of skills like Cooking, Cleaning, Laundry, Babysitting."""
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Househelp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='househelp')
    experience_years = models.IntegerField(default=0)
    
    # Change 1: Implementation of Skills as ManyToManyField (Strategy 2)
    skills = models.ManyToManyField(SkillTag, blank=True)
    
    # Change 2: Fixing Bio Help Text
    bio = models.TextField(max_length=500, blank=True, null=True, help_text="A summary of your experience and the services you provide.")
    
    availability_schedule = models.CharField(max_length=255, blank=True, null=True)
    expected_salary = models.IntegerField(default=0)
    
    # Change 5: Added by the user
    rating = models.FloatField(default=0.0)
    review_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Help: {self.user.email}"
