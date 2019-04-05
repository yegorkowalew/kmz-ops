# Generated by Django 2.2 on 2019-04-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeworker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tworker',
            name='not_processed_rows',
            field=models.PositiveIntegerField(help_text='Удаленные строки', verbose_name='Удаленные строки'),
        ),
        migrations.AlterField(
            model_name='tworker',
            name='yes_processed_rows',
            field=models.PositiveIntegerField(help_text='Добавленные строки', verbose_name='Добавленные строки'),
        ),
    ]
