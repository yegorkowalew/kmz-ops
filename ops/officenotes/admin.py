from django.contrib import admin

# Register your models here.
from .models import OfficeNote

class OfficeNoteAdmin(admin.ModelAdmin):
    fields = (('num', 'oncustomer'), ('date', 'datereceiving'), 'filepath')
    list_display = ('num', 'oncustomer', 'date', 'datereceiving', 'filepath')
    search_fields = ['num']

admin.site.register(OfficeNote, OfficeNoteAdmin)