# from testapp.models import StandartDetailCreator
from officenotes.models import OfficeNote
from order.models import Order
from customer.models import Customer

from random import randint
import openpyxl
import os
myhost = os.environ['COMPUTERNAME']

# 1. Удалить:
#     Компании
#     Служебные записки
#     Заказы

# 2. Добавить
#     Из Служебных записок - notes
#     Из Плана производства
#     Из Графика Количества

if myhost == "BOB":
    files_list = {'notes':'C:\\Users\\Yegor\\Dropbox\\ПДО_Производство\\Служебные записки.xlsx'}
elif myhost == "pdo-pro":
    files_list = {'notes':'Z:\\Служебные записки.xlsx'}

class Unit:
    def __init__(self, tableid, shipment_from, shipment_to, product, counterparty, ordernum, quantity, firstofficenote, otherofficenote, date, datereceiving, pickingplan, pickingpercent, pickingfact, shippingplan, shippingpercent, shippingfact, engineeringplan, engineeringpercent, engineeringfact, drawingchangepercent, drawingchangefact, materialplan, materialfact):
        """Constructor for Unit"""
        self.tableid = tableid # id в таблице 
        self.shipment_from = shipment_from # Отгрузка от 
        self.shipment_to = shipment_to # Отгрузка до 
        self.product = product # продукция 
        self.counterparty = counterparty # контрагент 
        self.ordernum = ordernum # № Заказа 
        self.quantity = quantity # Кол-во 
        self.firstofficenote = firstofficenote # № СЗ 
        self.otherofficenote = otherofficenote # № СЗ с изменениями 
        self.date = date # Дата СЗ 
        self.datereceiving = datereceiving # Дата СЗ Факт 
        self.pickingplan = pickingplan # Комплектовочные План 
        self.pickingpercent = pickingpercent # Комплектовочные % 
        self.pickingfact = pickingfact # Комплектовочные Факт 
        self.shippingplan = shippingplan # Отгрузочные План 
        self.shippingpercent = shippingpercent # Отгрузочные % 
        self.shippingfact = shippingfact # Отгрузочные Факт 
        self.engineeringplan = engineeringplan # Конструкторская План 
        self.engineeringpercent = engineeringpercent # Конструкторская % 
        self.engineeringfact = engineeringfact # Конструкторская Факт 
        self.drawingchangepercent = drawingchangepercent # Изменения чертежей % 
        self.drawingchangefact = drawingchangefact # Изменения чертежей Факт 
        self.materialplan = materialplan # Материалы План 
        self.materialfact = materialfact # Материалы Факт 

def append_notes(fpath):
    try:
        work_wb = openpyxl.load_workbook(filename=fpath)
    except:
        print('trabl')
        exit(0)
    sheet = work_wb['Просчет']
    nunits = []
    for row in range(2, sheet.max_row+1):#sheet.max_row+1):
        unit = Unit(
            sheet.cell(row=row, column=2).value,
            sheet.cell(row=row, column=4).value,
            sheet.cell(row=row, column=5).value,
            sheet.cell(row=row, column=8).value,
            sheet.cell(row=row, column=9).value,
            sheet.cell(row=row, column=10).value,
            sheet.cell(row=row, column=11).value,
            sheet.cell(row=row, column=12).value,
            sheet.cell(row=row, column=13).value,
            sheet.cell(row=row, column=15).value,
            sheet.cell(row=row, column=16).value,
            sheet.cell(row=row, column=20).value,
            sheet.cell(row=row, column=21).value,
            sheet.cell(row=row, column=22).value,
            sheet.cell(row=row, column=26).value,
            sheet.cell(row=row, column=27).value,
            sheet.cell(row=row, column=28).value,
            sheet.cell(row=row, column=32).value,
            sheet.cell(row=row, column=33).value,
            sheet.cell(row=row, column=34).value,
            sheet.cell(row=row, column=36).value,
            sheet.cell(row=row, column=37).value,
            sheet.cell(row=row, column=38).value,
            sheet.cell(row=row, column=39).value,
            )
        nunits.append(unit)
    work_wb.close()
    cust = [
        Order(
            product = nunit.product,
            tableid = nunit.tableid,

            shipmentfrom = nunit.shipment_from,
            shipmentto = nunit.shipment_to,
            ordernum = nunit.ordernum,
            quantity = nunit.quantity,
            pickingplan = nunit.pickingplan,
            pickingpercent = nunit.pickingpercent,
            pickingfact = nunit.pickingfact,
            shippingplan = nunit.shippingplan,
            shippingpercent = nunit.shippingpercent,
            shippingfact = nunit.shippingfact,
            engineeringplan = nunit.engineeringplan,
            engineeringpercent = nunit.engineeringpercent,
            engineeringfact = nunit.engineeringfact,
            drawingchangepercent = nunit.drawingchangepercent,
            drawingchangefact = nunit.drawingchangefact,
            materialplan = nunit.materialplan,
            materialfact = nunit.materialfact,

            firstofficenote = OfficeNote.objects.get_or_create(
                num = nunit.firstofficenote,
                date = nunit.date,
                datereceiving = nunit.datereceiving,
                oncustomer = Customer.objects.get_or_create(
                    name = nunit.counterparty
                    )[0]
                )[0]
            )
        for nunit in nunits
    ]
    custom = Order.objects.bulk_create(cust)

def append_base(flist):
    for name_model, fpath in flist.items():
        if name_model == 'notes':
            append_notes(fpath)

def delete_base():
    zz = Customer.objects.all().delete()
    log = ''
    log += 'Удалено %s записей из Теста' % zz[0]
    log += ''
    return log


def update():
    log_text = ''
    log = delete_base()
    append_base(files_list)
    yes_processed_rows=randint(1, 1000)
    not_processed_rows=randint(1, 1000)
    log_text += log
    return yes_processed_rows, not_processed_rows, log_text

# customers = {}
# for nunit in nunits:
#     if nunit.counterparty in customers:
#             customer = customers[nunit.counterparty]
#     else:
#         customer, _ = Customer.objects.get_or_create(
#                 name = nunit.counterparty
#             )
#         customers[nunit.counterparty] = customer
#     officenote, _ = OfficeNote.objects.get_or_create(
#             num = nunit.firstofficenote,
#             date = nunit.date,
#             datereceiving = nunit.datereceiving,
#             oncustomer = customer
#         )
#     norder = Order(
#         product = nunit.product,
#         tableid = nunit.tableid,
#         firstofficenote = officenote
#     )
#     norder.save()