from testapp.models import StandartDetailCreator

from random import randint

# 1. Удалить:
#     Компании
#     Служебные записки
#     Заказы

# 2. Добавить
#     Из Служебных записок
#     Из Плана производства
#     Из Графика Количества

def delete_base():
    zz = StandartDetailCreator.objects.all().delete()
    log = ''
    log += 'Удалено %s записей из Теста' % zz[0]
    return log


def update():
    log_text = ''
    log = delete_base()
    yes_processed_rows=randint(1, 1000)
    not_processed_rows=randint(1, 1000)
    log_text += log
    return yes_processed_rows, not_processed_rows, log_text