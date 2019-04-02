from testapp.models import StandartDetailCreator

from random import randint
import openpyxl

# 1. Удалить:
#     Компании
#     Служебные записки
#     Заказы

# 2. Добавить
#     Из Служебных записок - notes
#     Из Плана производства
#     Из Графика Количества

files_list = {'notes':'C:\\Users\\Yegor\\Dropbox\\ПДО_Производство\\Служебные записки.xlsx'}

class Unit:
    def __init__(self, fid, shipment_from, shipment_to, product, counterparty, order_number, amount, sz):
        """Constructor for Unit"""
        self.fid = fid # id
        self.shipment_from = shipment_from # Отгрузка от
        self.shipment_to = shipment_to # Отгрузка до
        self.product = product # продукция
        self.counterparty = counterparty # контрагент
        self.order_number = order_number # № Заказа
        self.amount = amount # Кол-во
        self.sz = sz # № СЗ

def append_notes(fpath):
    try:
        work_wb = openpyxl.load_workbook(filename=fpath)
    except:
        print('trabl')
        exit(0)
    sheet = work_wb['Просчет']
    for row in range(2, sheet.max_row):#sheet.max_row+1):
        print(sheet.cell(row=row, column=8).value)
        unit = Unit(
            sheet.cell(row=row, column=2).value,
            sheet.cell(row=row, column=4).value,
            sheet.cell(row=row, column=5).value,
            sheet.cell(row=row, column=8).value,
            sheet.cell(row=row, column=9).value,
            sheet.cell(row=row, column=10).value,
            sheet.cell(row=row, column=11).value,
            sheet.cell(row=row, column=12).value,
            )
        detail = StandartDetailCreator(fid = unit.fid, shipment_from = unit.shipment_from, shipment_to = unit.shipment_to, product = unit.product, counterparty = unit.counterparty, order_number = unit.order_number, amount = unit.amount, sz = unit.sz)
        detail.save()

def append_base(flist):
    for name_model, fpath in flist.items():
        if name_model == 'notes':
            append_notes(fpath)

def delete_base():
    zz = StandartDetailCreator.objects.all().delete()
    log = ''
    log += 'Удалено %s записей из Теста' % zz[0]
    return log


def update():
    log_text = ''
    log = delete_base()
    append_base(files_list)
    yes_processed_rows=randint(1, 1000)
    not_processed_rows=randint(1, 1000)
    log_text += log
    return yes_processed_rows, not_processed_rows, log_text