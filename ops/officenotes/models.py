from django.db import models

from customer.models import Customer

class OfficeNote(models.Model):
    num = models.PositiveIntegerField(
                            verbose_name="Номер служебной записки",
                            null = True,
                            blank = True,
                            unique=True,
                            help_text="Номер служебной записки"
                            )
    date = models.DateField(
                            verbose_name="Дата служебной записки", 
                            help_text="Дата служебной записки, указаннная в ней", 
                            null = True,
                            blank = True,
                            )
    datereceiving = models.DateField(
                            verbose_name="Дата получения служебной записки", 
                            help_text="Дата получения служебной записки, указанная в почте", 
                            null = True,
                            blank = True,
                            )
    oncustomer = models.ForeignKey(
                            Customer,
                            verbose_name="Заказчик",
                            max_length=50,
                            on_delete=models.CASCADE,
                            help_text='Заказчик',
                            )

    def __unicode__(self):
        return self.num % self.id

    def __str__(self):
            return '%s' % self.num

    def get_absolute_url(self):
        return "/office-note/%i/" % self.id

    class Meta:
        ordering = ["num"]
        verbose_name = "служебную записку"
        verbose_name_plural = "Служебные записки"