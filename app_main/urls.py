from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page),
    path('users/', views.users_page),
    path('my-posts/', views.my_posts),
    path('posts/', views.all_posts),
    path('posts/<int:post_id>/', views.post_detail),
    path('new-post/', views.post_create),
]
