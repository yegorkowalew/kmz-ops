from django.contrib import admin

# Register your models here.
from .models import OfficeNote

class OfficeNoteAdmin(admin.ModelAdmin):
    fields = (('num', 'oncustomer'), ('date', 'datereceiving'))
    list_display = ('num', 'oncustomer', 'date', 'datereceiving')
    search_fields = ['num']

admin.site.register(OfficeNote, OfficeNoteAdmin)