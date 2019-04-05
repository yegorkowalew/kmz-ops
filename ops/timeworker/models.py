from django.db import models

class TWorker(models.Model):
    date_start = models.DateTimeField(
                            verbose_name="Начало работ", 
                            )
    date_end = models.DateTimeField(
                            verbose_name="Окончание работ", 
                            )
    yes_processed_rows = models.PositiveIntegerField(
                            verbose_name="Добавленные строки",
                            help_text="Добавленные строки"
                            )
    not_processed_rows = models.PositiveIntegerField(
                            verbose_name="Удаленные строки",
                            help_text="Удаленные строки"
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