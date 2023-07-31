from django.db import models


class TodoModel(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        PROGRESS = 'Progress', 'Progress'
        DONE = 'Done', 'Done'

    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default='Active'
    )

    title = models.CharField(verbose_name='Название задачи', max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
