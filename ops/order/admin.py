from django.contrib import admin

from .models import Order

class MemberShopInlineAdmin(admin.TabularInline):
    model = Order.otherofficenote.through

class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основное', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('ready'), ('tableid', 'firstofficenote'), ('product', 'ordernum', 'quantity'),),
        }),
        ('Отгрузка', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('shipmentfrom', 'shipmentto'),),
        }),
        ('Комплектовочные', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('pickingplan', 'pickingpercent', 'pickingfact'),),
        }),
        ('Отгрузочные', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('shippingplan', 'shippingpercent', 'shippingfact'),),
        }),
        ('Конструкторские', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('engineeringplan', 'engineeringpercent', 'engineeringfact'),),
        }),
        ('Изменение чертежей', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('drawingchangepercent', 'drawingchangefact'),),
        }),
        ('Материалы', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('materialplan', 'materialfact'),),
        }),
        )
    readonly_fields = (
        'ready', 'tableid', 'firstofficenote', 
        'product', 'ordernum', 'quantity',
        'shipmentfrom', 'shipmentto', 
        'pickingplan', 'pickingpercent', 'pickingfact', 
        'shippingplan', 'shippingpercent', 'shippingfact', 
        'engineeringplan', 'engineeringpercent', 'engineeringfact', 
        'drawingchangepercent', 'drawingchangefact', 'materialplan', 
        'materialfact', 
        )
    list_display = ('ordernum', 'tableid', 'product', 'quantity', 'get_name', 'ready',)
    search_fields = ['ordernum']
    inlines = [MemberShopInlineAdmin]
    def get_name(self, obj):
        return obj.firstofficenote.oncustomer.name
    # get_name.admin_order_field  = 'author'  #Allows column order sorting
    get_name.short_description = 'Заказчик'  #Renames column head

admin.site.register(Order, OrderAdmin)