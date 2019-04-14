from django.db import models
from order.models import Order

from datetime import datetime
from datetime import timedelta

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

    def get_to_work_days(self):
        nowday = datetime.now().date()
        if self.datestart and self.dateend:
            return (self.datestart - nowday).days
        else:
            return None

    def get_to_endwork_days(self):
        nowday = datetime.now().date()
        if self.datestart and self.dateend:
            return (self.dateend - nowday).days
        else:
            return None

    def get_work_days(self):
        if self.datestart and self.dateend:
            return (self.dateend - self.datestart).days
        else:
            return None

    def get_day_in_work(self):
        if self.datestart and self.dateend:
            nowday = datetime.now().date()
            return (nowday - self.datestart).days
        else:
            return None

    def get_day_in_work_percent(self):
        if self.datestart and self.dateend:
            nowday = datetime.now().date()
            print('Дней в работе ', (nowday - self.datestart).days)
            print('Дней работы ', (self.dateend - self.datestart).days)
            return round(((nowday - self.datestart).days*100)/(self.dateend - self.datestart).days)
        else:
            return None

    def get_work(self):
        if self.datestart and self.dateend:
            nowday = datetime.now().date()
            # to_work_days = (self.datestart - nowday).days # get_to_work_days дней до начала работы
            # to_endwork_days = (self.dateend - nowday).days # get_to_endwork_days дней до конца работы
            work_days = (self.dateend - self.datestart).days+1 #get_work_days дней в работе
            day_in_work = (nowday - self.datestart).days+1 #get_day_in_work прошло дней с начала работы
            percent = round(((nowday - self.datestart).days*100)/((self.dateend - self.datestart).days+1)) #get_day_in_work_percent прошло дней с начала работы в процентах 

            if day_in_work >= work_days:
                day_in_work = work_days
                percent = 100 
            return {
                'to_work_days': (self.datestart - nowday).days, # get_to_work_days дней до начала работы 
                'to_endwork_days': (self.dateend - nowday).days+1, # get_to_endwork_days дней до конца работы
                'work_days': (self.dateend - self.datestart).days+1, #get_work_days дней в работе
                'day_in_work': day_in_work, #get_day_in_work прошло дней с начала работы
                'percent': percent, #get_day_in_work_percent прошло дней с начала работы в процентах 
                }
        else:
            return None

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