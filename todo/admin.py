from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class Todo(admin.ModelAdmin):
    list_display = ['title', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'created_at']
