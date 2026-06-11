from django.db import models


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('progress', 'В работе'),
        ('done', 'Обработана'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Review(models.Model):
    author = models.CharField(max_length=100)

    rating = models.PositiveSmallIntegerField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]
    )

    text = models.TextField(max_length=1000)

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} ({self.rating})"