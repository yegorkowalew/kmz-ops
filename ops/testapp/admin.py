from django.contrib import admin

from .models import StandartDetailCreator
class StandartDetailCreatorAdmin(admin.ModelAdmin):
    fields = ('product', 'fid', 'shipment_from', 'shipment_to', 'counterparty', 'order_number', 'amount', 'sz')
    list_display = ('product', 'fid', 'shipment_from', 'shipment_to', 'counterparty', 'order_number', 'amount', 'sz')


admin.site.register(StandartDetailCreator, StandartDetailCreatorAdmin)