from django.db import models


class Period(models.Model):
    name = models.CharField(max_length=10, verbose_name='Периодичность')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Периодичность'
        verbose_name_plural = 'Периоды'
