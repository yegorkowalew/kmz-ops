from django.template.response import TemplateResponse
import logging

from officenotes.models import OfficeNote
from order.models import Order
from timeworker.models import TWorker
from datetime import datetime
from datetime import timedelta
from django.views.generic.detail import DetailView

logger = logging.getLogger('catalog')

def index(request):
    """
    Главная страница.
    """
    title = "Главная"

    nowday = datetime.now()
    day_add_ten_days = nowday+timedelta(days=10)
    all_orders = Order.objects.all()
    len_orders = all_orders.count()
    len_ready_orders = all_orders.filter(ready=True).count()
    len_min_ten = all_orders.filter(ready=False).filter(shipmentto__lte=day_add_ten_days).count()
    len_max_ten = all_orders.filter(ready=False).filter(shipmentto__gte=day_add_ten_days).count()
    len_pros = all_orders.filter(ready=False).filter(shipmentto__lte=nowday).count()
    # Все заказы - 
    # Готовые - 
    # Просроченные -
    # Меньше 10 дней - 
    # Больше 10 дней - 
    # print('---',len_max_ten)
    # print('--',len_min_ten)
    # print('-',len_pros)
    
    
    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'index.html', {
                                                    'title':title, 
                                                    'len_notes':OfficeNote.objects.all().count(),
                                                    'len_orders':len_orders, # Все заказы
                                                    'len_ready_orders':len_ready_orders, # Готовые
                                                    'len_max_ten':len_max_ten, # Больше 10 дней
                                                    'len_min_ten':len_min_ten, # Меньше 10 дней
                                                    'len_pros':len_pros, # Просроченные
                                                    })

def classic_ops(request):
    """
    Классический оперативный производственный график
    """
    title = "Классический оперативный производственный график"

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'classic_ops.html', {
                                                    'title':title, 
                                                    'orders':Order.objects.all(),
                                                    'rebild':TWorker.objects.last()
                                                    })

class OfficeNoteDetailView(DetailView):
    model = OfficeNote
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        firstofficenotes = Order.objects.filter(firstofficenote__num=self.object.num)
        otherofficenotes = Order.objects.filter(otherofficenote__num=self.object.num)
        if list(firstofficenotes)>list(otherofficenotes):
            context['orders'] = firstofficenotes
        else:
            context['orders'] = otherofficenotes
        context['rebild'] = TWorker.objects.last()
        return context