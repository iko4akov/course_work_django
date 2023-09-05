from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='Адрес', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(verbose_name='Изображение', **NULLABLE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    public = models.BooleanField(verbose_name='Признак публикации')
    count_view = models.IntegerField(default=0, verbose_name='Просмотры')

    user = models.ForeignKey('user.User', related_name='user', on_delete=models.CASCADE, **NULLABLE)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title', )
