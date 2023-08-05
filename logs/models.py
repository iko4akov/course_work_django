from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}


class Logs(models.Model):

    try_last = models.DateTimeField(default=timezone.now)
    send = models.ForeignKey('send.Send', on_delete=models.CASCADE)
    respounse = models.CharField(**NULLABLE)

    def __str__(self):
        return f'{self.try_last}'
    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
