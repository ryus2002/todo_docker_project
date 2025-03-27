from django.contrib import admin
from .models import Task, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'due_date', 'completed')
    list_filter = ('completed', 'priority', 'category', 'user')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
