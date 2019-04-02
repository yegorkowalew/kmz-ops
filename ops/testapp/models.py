from django.db import models

class StandartDetailCreator(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Название", 
                            )
    edit_date = models.DateField(
                            verbose_name="Последнее изменение", 
                            auto_now=True,
                            )
    class Meta:
        verbose_name = ("Родитель стандартной детали")
        verbose_name_plural = ("Родители стандартной детали")

    def __str__(self):
        return self.name
