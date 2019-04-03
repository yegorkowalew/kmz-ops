from django.db import models

from officenotes.models import OfficeNote

class Order(models.Model):
    shipmentfrom = models.DateField(
                            verbose_name='Отгрузка "от"', 
                            help_text="Дата служебной записки, указаннная в ней"
                            )
    shipmentto = models.DateField(
                            verbose_name='Отгрузка "до"', 
                            help_text="Дата служебной записки, указаннная в ней"
                            )
    
    product = models.CharField(
                            verbose_name="Продукция", 
                            max_length=100,
                            help_text="Название продукта"
                            )
    ordernum = models.PositiveIntegerField(
                            verbose_name="№ Заказа",
                            null = True,
                            blank = True,
                            # unique=True,
                            help_text="Оригинальный номер папки"
                            )
    quantity= models.FloatField(
                            verbose_name="Кол-во",
                            null = True,
                            blank = True,
                            # unique=True,
                            help_text="Количество изделий"
                            )    
    pickingplan = models.DateField(
                            verbose_name="Комплектовочные План", 
                            help_text="Комплектовочные План",
                            null = True,
                            blank = True
                            )
    pickingpercent = models.PositiveIntegerField(
                            verbose_name="Комплектовочные %",
                            null = True,
                            blank = True,
                            help_text="Комплектовочные %"
                            )
    pickingfact = models.DateField(
                            verbose_name="Комплектовочные Факт", 
                            help_text="Комплектовочные Факт",
                            null = True,
                            blank = True
                            )
    shippingplan = models.DateField(
                            verbose_name="Отгрузочные План", 
                            help_text="Отгрузочные План",
                            null = True,
                            blank = True
                            )
    shippingpercent = models.PositiveIntegerField(
                            verbose_name="Отгрузочные %",
                            null = True,
                            blank = True,
                            help_text="Отгрузочные %"
                            )
    shippingfact = models.DateField(
                            verbose_name="Отгрузочные Факт", 
                            help_text="Отгрузочные Факт",
                            null = True,
                            blank = True
                            )
    engineeringplan = models.DateField(
                            verbose_name="Конструкторская План", 
                            help_text="Конструкторская План",
                            null = True,
                            blank = True
                            )
    engineeringpercent = models.PositiveIntegerField(
                            verbose_name="Конструкторская %",
                            null = True,
                            blank = True,
                            help_text="Конструкторская %"
                            )
    engineeringfact = models.DateField(
                            verbose_name="Конструкторская Факт", 
                            help_text="Конструкторская Факт",
                            null = True,
                            blank = True
                            )
    drawingchangepercent = models.PositiveIntegerField(
                            verbose_name="Изменения чертежей %",
                            null = True,
                            blank = True,
                            help_text="Изменения чертежей %"
                            )
    drawingchangefact = models.DateField(
                            verbose_name="Изменения чертежей Факт", 
                            help_text="Изменения чертежей Факт",
                            null = True,
                            blank = True
                            )
    materialplan = models.DateField(
                            verbose_name="Материалы План", 
                            help_text="Материалы План",
                            null = True,
                            blank = True
                            )
    materialfact = models.DateField(
                            verbose_name="Материалы Факт", 
                            help_text="Материалы Факт",
                            null = True,
                            blank = True
                            )
    tableid = models.PositiveIntegerField(
                            verbose_name="id в таблице",
                            unique=True,
                            help_text="id в таблице"
                            )
    firstofficenote = models.ForeignKey(
                            OfficeNote,
                            verbose_name="Служебная записка",
                            max_length=50,
                            on_delete=models.CASCADE,
                            help_text='Служебная записка',
                            )
    otherofficenote = models.ManyToManyField(
                            OfficeNote,
                            verbose_name="Дополнительные служебные записки",
                            blank = True,
                            related_name='officenotes'
                            )

    def __unicode__(self):
        return self.product % self.id

    def __str__(self):
            return '%s' % self.product

    def get_absolute_url(self):
        return "/order/%i/" % self.id

    class Meta:
        ordering = ["ordernum"]
        verbose_name = "заказ"
        verbose_name_plural = "заказы"