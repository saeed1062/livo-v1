from django.contrib import admin
from .models import Apartment

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rent_amount', 'owner', 'created_at')
    list_filter = ('city', 'has_wifi', 'has_parking', 'has_ac')
    search_fields = ('name', 'address', 'city', 'owner__username')
    ordering = ('-created_at',)
