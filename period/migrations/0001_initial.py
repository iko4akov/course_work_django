# Generated by Django 4.2.3 on 2023-07-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Периодичность')),
            ],
            options={
                'verbose_name': 'Периодичность',
                'verbose_name_plural': 'Периоды',
            },
        ),
    ]
