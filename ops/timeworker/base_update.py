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

def append_notes(fpath):
    try:
        work_wb = openpyxl.load_workbook(filename=fpath)
    except:
        print('trabl')
        exit(0)
    sheet = work_wb['Просчет']
    for row in range(3, sheet.max_row+1):
        print(sheet.cell(row=row, column=8).value)
        detail = StandartDetailCreator(name=sheet.cell(row=row, column=8).value)
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