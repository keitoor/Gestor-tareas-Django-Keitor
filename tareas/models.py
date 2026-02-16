from django.db import models

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Lista de tareas"
        verbose_name_plural = "Listas de tareas"
class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"