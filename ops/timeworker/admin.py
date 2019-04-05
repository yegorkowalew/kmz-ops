from django.contrib import admin

from .models import TWorker
from datetime import datetime
import time

from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .base_update import update

def make_tworker(modeladmin, request, queryset):
    b = TWorker(date_start=datetime.now())
    b.yes_processed_rows, b.not_processed_rows, b.log_text = update()
    b.date_end=datetime.now()
    b.save()
make_tworker.short_description = "Обновление базы"

class TWorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start_f', 'date_end_f', 'days_between', 'yes_processed_rows', 'not_processed_rows')
    readonly_fields = ('id', 'date_start_f', 'date_end_f', 'yes_processed_rows', 'not_processed_rows', 'log_text', 'date_start_f')
    actions = [make_tworker]
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'make_tworker':
            if not request.POST.getlist(admin.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in TWorker.objects.all():
                    post.update({admin.ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(TWorkerAdmin, self).changelist_view(request, extra_context)

    def date_start_f(self, instance):
        return mark_safe("<span>%s</span>" % instance.date_start.strftime("%d.%m.%Y %H:%M:%S"))
    date_start_f.short_description = "Начало работ"

    def date_end_f(self, instance):
        return mark_safe("<span>%s</span>" % instance.date_end.strftime("%d.%m.%Y %H:%M:%S"))
    date_end_f.short_description = "Начало работ"

    def days_between(self, instance):
        return abs((instance.date_end - instance.date_start).seconds)
    days_between.short_description = "Секунд"

admin.site.register(TWorker, TWorkerAdmin)