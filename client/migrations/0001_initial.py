# Generated by Django 4.2.4 on 2023-08-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фамилия')),
                ('third_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('comment', models.TextField(verbose_name='Коментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
