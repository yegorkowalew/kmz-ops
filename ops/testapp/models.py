from django.db import models

class StandartDetailCreator(models.Model):
    fid = models.PositiveIntegerField(
                            verbose_name="ID",
                            help_text="ID",
                            blank = True,
                            null = True
                            )
    shipment_from = models.DateField(
                            verbose_name="Отгрузка от", 
                            blank = True,
                            null = True
                            )
    shipment_to = models.DateField(
                            verbose_name="Отгрузка до", 
                            blank = True,
                            null = True
                            )
    product = models.CharField(max_length=100,
                            verbose_name="продукция", 
                            )
    counterparty = models.CharField(max_length=50,
                            verbose_name="контрагент", 
                            blank = True,
                            null = True
                            )
    order_number = models.PositiveIntegerField(
                            verbose_name="№ Заказа",
                            help_text="№ Заказа",
                            blank = True,
                            null = True
                            )
    amount = models.PositiveIntegerField(
                            verbose_name="Кол-во",
                            help_text="Кол-во",
                            blank = True,
                            null = True
                            )
    sz = models.PositiveIntegerField(
                            verbose_name="СЗ",
                            help_text="СЗ",
                            blank = True,
                            null = True
                            )
    class Meta:
        ordering = ["fid"]
        verbose_name = ("Заказ")
        verbose_name_plural = ("Заказ")

    def __str__(self):
        return self.product
        # self.fid = fid # id
        # self.shipment_from = shipment_from # Отгрузка от
        # self.shipment_to = shipment_to # Отгрузка до
        # self.products = products # продукция
        # self.counterparty = counterparty # контрагент
        # self.order_number = order_number # № Заказа
        # self.amount = amount # Кол-во
        # self.sz = sz # № СЗ