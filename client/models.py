from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=200, verbose_name='Фамилия', **NULLABLE)
    third_name = models.CharField(max_length=200, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(verbose_name='Почта', unique=True)
    comment = models.TextField(verbose_name='Коментарий')

    def __str__(self):
        name_slice = lambda x: x[0]+'.' if x else None
        return f'{self.second_name} {name_slice(self.first_name)}.{name_slice(self.third_name)}.'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
