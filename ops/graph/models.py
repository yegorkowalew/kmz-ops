from django.db import models
from order.models import Order

class Workshop(models.Model):
    numname = models.PositiveIntegerField(
        verbose_name="Номер цеха",
        help_text="Номер цеха",
        unique = True
        )
    name = models.CharField(
        verbose_name="Название",
        help_text="Словесное обозначение цеха", 
        max_length=100,
        blank = True,
        null = True
        )
    fullname = models.CharField(
        verbose_name="Полное название",
        help_text="Полное словесное обозначение цеха", 
        max_length=200,
        blank = True,
        null = True
        )

    def __unicode__(self):
        return "%s (%s)" % (self.numname, self.name)

    def __str__(self):
        return "%s" % self.numname

    def get_absolute_url(self):
        return "/workshop/%i/" % self.numname

    class Meta:
        ordering = ["numname"]
        verbose_name = "Цех"
        verbose_name_plural = "Цех"

class DateRange(models.Model):
    workshop = models.ForeignKey(
        Workshop,
        verbose_name="Цех",
        help_text='Цех',
        max_length=50,
        on_delete=models.CASCADE,
        )
    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        help_text='Заказ',
        max_length=50,
        on_delete=models.CASCADE,
        )
    datestart = models.DateField(
        verbose_name="Дата начала", 
        help_text="Дата начала"
        )
    dateend = models.DateField(
        verbose_name="Дата окончания", 
        help_text="Дата окончания"
        )
    def __unicode__(self):
        return "%s" % (self.pk)

    def __str__(self):
        return "%s - %s (%s)" % (self.workshop.numname, self.order.ordernum, self.order.product)

    def get_absolute_url(self):
        return "/daterange/%i/" % self.pk

    class Meta:
        ordering = ["order"]
        verbose_name = "Период дат"
        verbose_name_plural = "Период дат"

# class DatePeriod(models.Model):
#     datestart = models.DateField(
#         verbose_name="Дата начала", 
#         help_text="Дата начала"
#         )
#     dateend = models.DateField(
#         verbose_name="Дата окончания", 
#         help_text="Дата окончания"
#         )
#     daterange = models.ForeignKey(
#         DateRange,
#         verbose_name="Период дат",
#         help_text="Период дат",
#         max_length=50,
#         on_delete=models.CASCADE,
#         )

#     class Meta:
#         ordering = ["pk"]
#         verbose_name = "Период"
#         verbose_name_plural = "Период"