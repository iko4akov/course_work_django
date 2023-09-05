from django.db import models

class Mailing(models.Model):

    client = models.ForeignKey('client.Client', on_delete=models.CASCADE, verbose_name='client')
    send = models.ForeignKey('send.Send', on_delete=models.CASCADE, verbose_name='send')

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='user')

    def __str__(self):
        return f'{self.client} - {self.send}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылка'


