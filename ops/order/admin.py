from django.contrib import admin

from .models import Order

class MemberShopInlineAdmin(admin.TabularInline):
    model = Order.otherofficenote.through

class OrderAdmin(admin.ModelAdmin):
    fields = ('ready', ('shipmentfrom', 'shipmentto'), 
            ('product', 'ordernum', 'quantity'), 
            ('pickingplan', 'pickingpercent', 'pickingfact'), 
            ('shippingplan', 'shippingpercent', 'shippingfact'), 
            ('engineeringplan', 'engineeringpercent', 'engineeringfact'), 
            ('drawingchangepercent', 'drawingchangefact'), 
            ('materialplan', 'materialfact'), 
            ('tableid', 'firstofficenote'))
    list_display = ('tableid', 'product', 'ordernum', 'quantity')
    search_fields = ['product']
    inlines = [MemberShopInlineAdmin]

admin.site.register(Order, OrderAdmin)