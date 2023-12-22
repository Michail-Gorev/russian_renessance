from django.contrib.auth.models import User
from django.db import models

from toursPage.models import Tour


# Create your models here.
class Feedback(models.Model):
    username = models.CharField('Имя пользователя', max_length=255, default='Имя')
    text = models.TextField('Текст отзыва', max_length=30000, default='Текст отзыва')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, default=None, related_name='Тур')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

