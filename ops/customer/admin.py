from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    fields = (['name'])
    readonly_fields = ('name',)
    list_display = (['name'])
    search_fields = ['name']

admin.site.register(Customer, CustomerAdmin)