from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('task/add/', views.add_task, name='add_task'),
    path('task/edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('task/complete/<int:pk>/', views.complete_task, name='complete_task'),
    path('category/add/', views.add_category, name='add_category'),
]
