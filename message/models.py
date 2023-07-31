from django.db import models


class Message(models.Model):
    theme = models.CharField(max_length=50, verbose_name='Тема')
    message = models.CharField(max_length=50, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
