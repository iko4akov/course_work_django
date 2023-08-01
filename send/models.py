from django.db import models


class Send(models.Model):
    params = models.ForeignKey('params.Message', on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, verbose_name='клиент')

    def __str__(self):
        return f'{self.pk} {self.client} - {self.params}'

    class Meta:
        verbose_name = 'Отправление'
        verbose_name_plural = 'Отправления'
