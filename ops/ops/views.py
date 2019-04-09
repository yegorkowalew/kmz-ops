from django.template.response import TemplateResponse
import logging

from officenotes.models import OfficeNote
from order.models import Order

logger = logging.getLogger('catalog')

def index(request):
    """
    Главная страница.
    """
    title = "Главная"

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'index.html', {
                                                    'title':title, 
                                                    'len_notes':OfficeNote.objects.all().count(),
                                                    'len_orders':Order.objects.all().count(),
                                                    'len_ready_orders':Order.objects.filter(ready=True).count(),
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
                                                    })