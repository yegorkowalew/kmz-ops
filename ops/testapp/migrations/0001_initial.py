# Generated by Django 2.2 on 2019-04-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StandartDetailCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('edit_date', models.DateField(auto_now=True, verbose_name='Последнее изменение')),
            ],
            options={
                'verbose_name': 'Родитель стандартной детали',
                'verbose_name_plural': 'Родители стандартной детали',
            },
        ),
    ]
