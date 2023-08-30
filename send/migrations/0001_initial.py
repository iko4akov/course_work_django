# Generated by Django 4.2.4 on 2023-08-29 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('message', '0001_initial'),
        ('period', '0001_initial'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время рассылки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.message', verbose_name='сообщение')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='period.period', verbose_name='период')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.status', verbose_name='статус')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылка',
            },
        ),
    ]
