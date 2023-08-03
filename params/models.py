from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Params(models.Model):
    time = models.TimeField(verbose_name='Время рассылки')
    period = models.ForeignKey('period.Period', on_delete=models.CASCADE, verbose_name='период')
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, verbose_name='статус')
    message = models.ForeignKey('message.Message', on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return f'{self.pk, self.time, self.message.theme}'

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'
