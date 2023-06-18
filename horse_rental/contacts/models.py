from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(blank=False, verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Пожелание'
        verbose_name_plural = 'Пожелания'

