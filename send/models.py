from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Send(models.Model):
    message = models.ForeignKey('message.Message', on_delete=models.CASCADE, verbose_name='сообщение')
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, verbose_name='статус', default='1')
    period = models.ForeignKey('period.Period', on_delete=models.CASCADE, verbose_name='период')
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, verbose_name='клиент')
    time = models.TimeField(verbose_name='Время рассылки')

    def __str__(self):
        return f'{self.pk} {self.message.theme}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'
