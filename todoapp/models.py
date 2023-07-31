from django.db import models


class TodoModel(models.Model):
    title = models.CharField(verbose_name='Название задачи', max_length=255)
    description = models.TextField()
    is_complete = models.BooleanField(verbose_name='Завершено', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
