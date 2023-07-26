from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=200, verbose_name='Фамилия', **NULLABLE)
    third_name = models.CharField(max_length=200, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(verbose_name='Почта', unique=True)
    comment = models.TextField(verbose_name='Коментарий')

    def __str__(self):
        return f'{self.second_name} {self.first_name[0]}.{self.third_name[0]}.'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    theme = models.CharField(max_length=50, verbose_name='Тема')
    message = models.CharField(max_length=50, verbose_name='Сообщение')

    def __str__(self):
        return f'{self.theme}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Period(models.Model):
    name = models.CharField(max_length=10, verbose_name='Периодичность')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Периодичность'
        verbose_name_plural = 'Периоды'


class Status(models.Model):
    name = models.CharField(max_length=10, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Distription(models.Model):

    time = models.TimeField(verbose_name='Время рассылки')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name='период')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return f'{self.time, self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Logs(models.Model):

    try_last = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey(Distription, on_delete=models.CASCADE)
    respounse = models.CharField(**NULLABLE)

    def __str__(self):
        return f'{self.try_last}'
