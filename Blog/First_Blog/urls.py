from . import views
from django.urls import path

urlpatterns = [
    path('', views.blog, name='blog'),
    path('create/', views.blog_create, name='blog_create'),
    path('edit/<int:pk>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    path('register/', views.register, name='register'),

]