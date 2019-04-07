from django.db import models

class TWorker(models.Model):
    date_start = models.DateTimeField(
                            verbose_name="Начало работ", 
                            null = True,
                            blank = True
                            )
    date_end = models.DateTimeField(
                            verbose_name="Окончание работ", 
                            null = True,
                            blank = True
                            )
    yes_processed_rows = models.PositiveIntegerField(
                            verbose_name="Обработанные строки",
                            null = True,
                            blank = True
                            )
    not_processed_rows = models.PositiveIntegerField(
                            verbose_name="Удаленные записи",
                            null = True,
                            blank = True
                            )
    log_text = models.TextField(
                            verbose_name="Лог",
                            null = True,
                            blank = True
                            )
    ready = models.BooleanField(
                            verbose_name='Работа завершена',
                            null = True,
                            blank = True
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