from django.contrib import admin

# Register your models here.

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    fields = (['name'])
    list_display = (['name'])
    search_fields = ['name']
    # inlines = (TermInlineAdmin, DetailInlineAdmin, StandartDetailInlineAdmin, UnitContentPhotoInlineAdmin)

admin.site.register(Customer, CustomerAdmin)