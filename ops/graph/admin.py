from django.contrib import admin

from .models import Workshop, DateRange

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('numname', 'name', 'fullname')
    # readonly_fields = ('numname', 'name', 'fullname')
    fields = ('numname', 'name', 'fullname')

# class DatePeriodAdmin(admin.ModelAdmin):
    # list_display = ('daterange', 'datestart', 'dateend')
    # readonly_fields = ('datestart', 'dateend', 'daterange')
    # fields = ('datestart', 'dateend', 'daterange')

class DateRangeAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'order', 'datestart', 'dateend')
    # readonly_fields = ('workshop', 'order')
    fields = ('workshop', 'order', 'datestart', 'dateend')

admin.site.register(Workshop, WorkshopAdmin)
# admin.site.register(DatePeriod, DatePeriodAdmin)
admin.site.register(DateRange, DateRangeAdmin)

