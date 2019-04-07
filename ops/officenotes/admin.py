from django.contrib import admin
from .models import OfficeNote

class OfficeNoteAdmin(admin.ModelAdmin):
    fields = (('num', 'oncustomer'), ('date', 'datereceiving'), 'filepath')
    list_display = ('num', 'oncustomer', 'date', 'datereceiving', 'filepath')
    readonly_fields = ('num', 'oncustomer', 'date', 'datereceiving', 'filepath')
    search_fields = ['num']

admin.site.register(OfficeNote, OfficeNoteAdmin)