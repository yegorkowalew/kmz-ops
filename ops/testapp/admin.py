from django.contrib import admin

from .models import StandartDetailCreator
# class StandartDetailCreatorAdmin(admin.ModelAdmin):
#     fields = ('name')

admin.site.register(StandartDetailCreator)