# Generated by Django 2.2 on 2019-04-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='standartdetailcreator',
            options={'ordering': ['fid'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказ'},
        ),
        migrations.RemoveField(
            model_name='standartdetailcreator',
            name='edit_date',
        ),
        migrations.RemoveField(
            model_name='standartdetailcreator',
            name='name',
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='amount',
            field=models.PositiveIntegerField(blank=True, help_text='Кол-во', null=True, verbose_name='Кол-во'),
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='counterparty',
            field=models.CharField(default=1, max_length=50, verbose_name='контрагент'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='fid',
            field=models.PositiveIntegerField(blank=True, help_text='ID', null=True, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='order_number',
            field=models.PositiveIntegerField(blank=True, help_text='№ Заказа', null=True, verbose_name='№ Заказа'),
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='product',
            field=models.CharField(default=1, max_length=100, verbose_name='продукция'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='shipment_from',
            field=models.DateField(blank=True, null=True, verbose_name='Отгрузка от'),
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='shipment_to',
            field=models.DateField(blank=True, null=True, verbose_name='Отгрузка до'),
        ),
        migrations.AddField(
            model_name='standartdetailcreator',
            name='sz',
            field=models.PositiveIntegerField(blank=True, help_text='СЗ', null=True, verbose_name='СЗ'),
        ),
    ]
