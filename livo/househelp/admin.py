from django.contrib import admin
from househelp.models import Househelp, SkillTag

# Register your models here.

@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Househelp)
class HousehelpAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_years', 'expected_salary', 'rating')
    list_filter = ('rating',)
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    filter_horizontal = ('skills',) # Better UI for selecting multiple skills from master list
