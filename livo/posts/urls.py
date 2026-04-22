from django.urls import path
from . import views

urlpatterns = [
    path('create-post/', views.create_post, name='create_post'),
    path('feed/<str:post_type>/', views.post_feed, name='feed'),
    
    # AJAX Interactions
    path('like/<int:post_id>/', views.toggle_like_ajax, name='toggle_like'),
    path('comment/<int:post_id>/', views.add_comment_ajax, name='add_comment'),
]
