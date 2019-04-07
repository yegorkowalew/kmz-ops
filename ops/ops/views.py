from django.template.response import TemplateResponse
import logging

logger = logging.getLogger('catalog')

def index(request):
    """
    Главная страница.
    """
    title = "Главная"
    admin_log = 'yo'

    logger.info('"%s" page visited. User: %s' % (title, request.user))
    return TemplateResponse(request, 'index.html', {'log': admin_log,
                                                    'title':title, 
                                                    })