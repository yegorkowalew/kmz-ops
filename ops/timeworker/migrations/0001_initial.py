# Generated by Django 2.2 on 2019-04-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Начало работ')),
                ('date_end', models.DateTimeField(verbose_name='Окончание работ')),
                ('yes_processed_rows', models.PositiveIntegerField(help_text='Удачно обработанные строки', verbose_name='Удачно обработанные строки')),
                ('not_processed_rows', models.PositiveIntegerField(help_text='Не удачно обработанные строки', verbose_name='Не удачно обработанные строки')),
                ('log_text', models.TextField(help_text='Лог', verbose_name='Лог')),
            ],
            options={
                'verbose_name': 'работу',
                'verbose_name_plural': 'работа',
                'ordering': ['id'],
            },
        ),
    ]
