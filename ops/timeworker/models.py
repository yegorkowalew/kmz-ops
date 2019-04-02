from django.db import models

class TWorker(models.Model):
    date_start = models.DateTimeField(
                            verbose_name="Начало работ", 
                            )
    date_end = models.DateTimeField(
                            verbose_name="Окончание работ", 
                            )
    yes_processed_rows = models.PositiveIntegerField(
                            verbose_name="Удачно обработанные строки",
                            help_text="Удачно обработанные строки"
                            )
    not_processed_rows = models.PositiveIntegerField(
                            verbose_name="Не удачно обработанные строки",
                            help_text="Не удачно обработанные строки"
                            )
    log_text = models.TextField(
                            verbose_name="Лог",
                            help_text="Лог"
                            )
    def __unicode__(self):
        return "%i" % self.id

    def __str__(self):
            return "%i" % self.id

    def get_absolute_url(self):
        return "/worker/%i/" % self.id

    class Meta:
        ordering = ["id"]
        verbose_name = "работу"
        verbose_name_plural = "работа"