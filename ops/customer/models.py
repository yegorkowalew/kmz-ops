from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(
                            max_length=50,
                            verbose_name="Название организации",
                            unique=True,
                            help_text="Название организации"
                            )

    def __unicode__(self):
        return self.name

    def __str__(self):
            return '%s' % self.name

    def get_absolute_url(self):
        return "/office-note/%i/" % self.id

    class Meta:
        ordering = ["name"]
        verbose_name = "Заказчика"
        verbose_name_plural = "Заказчики"