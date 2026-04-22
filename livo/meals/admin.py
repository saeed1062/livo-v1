from django.contrib import admin
from meals.models import MealProvider, Meal

# Register your models here.

@admin.register(MealProvider)
class MealProviderAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'rating', 'review_count')
    search_fields = ('user__email', 'location')
    list_filter = ('rating',)

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal_type', 'price', 'provider', 'post')
    list_filter = ('meal_type',)
    search_fields = ('name', 'post__title',)
