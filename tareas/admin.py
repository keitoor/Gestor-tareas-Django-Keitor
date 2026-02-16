from django.contrib import admin
from .models import TaskList, Task

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'               
    ordering = ('-created_at',)                    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'task_list', 'created_at')
    list_filter = ('completed', 'task_list')       
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    list_editable = ('completed',)                  