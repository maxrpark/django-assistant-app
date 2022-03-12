from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50, null=False)
    complete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        return self.title
