from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}

class Send(models.Model):
    message = models.ForeignKey('message.Message', on_delete=models.CASCADE, verbose_name='сообщение')
    status = models.ForeignKey('status.Status', on_delete=models.CASCADE, verbose_name='статус', default='1')
    period = models.ForeignKey('period.Period', on_delete=models.CASCADE, verbose_name='период')
    time = models.TimeField(verbose_name='Время рассылки', default=timezone.now)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return f'{self.pk} {self.message.theme} {self.status.name} {self.period.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'
        permissions = [
            (
                'set_status',
                'Can status send'
            )
        ]

