from django.contrib import admin
from posts.models import Post, ResidentRecord

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'user', 'availability', 'created_at')
    list_filter = ('type', 'availability')
    search_fields = ('title', 'description', 'user__username')

@admin.register(ResidentRecord)
class ResidentRecordAdmin(admin.ModelAdmin):
    list_display = ('resident', 'apartment', 'is_active', 'start_date')
    list_filter = ('is_active',)
    # FIXED: Apartment model uses 'name', not 'title'
    search_fields = ('resident__username', 'apartment__name')
