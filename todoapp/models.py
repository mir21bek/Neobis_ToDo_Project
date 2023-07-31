from django.db import models


class TodoModel(models.Model):
    title = models.CharField(verbose_name='Название задачи', max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
