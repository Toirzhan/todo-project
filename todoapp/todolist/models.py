from django.db import models

class ToDo(models.Model):
    title = models.CharField(
        verbose_name='Название задания',
        max_length=500
    )
    is_complete = models.BooleanField(
        verbose_name='Завершено',
        default=False
    )

    
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title