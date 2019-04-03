from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(
                            max_length=50,
                            verbose_name="Название организации",
                            unique=True,
                            null = True,
                            blank = True,
                            help_text="Название организации"
                            )

    def __unicode__(self):
        return self.pk

    def __str__(self):
            return '%s' % self.pk

    def get_absolute_url(self):
        return "/office-note/%i/" % self.pk

    class Meta:
        ordering = ["name"]
        verbose_name = "Заказчика"
        verbose_name_plural = "Заказчики"