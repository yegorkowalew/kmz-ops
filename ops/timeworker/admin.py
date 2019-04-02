from django.contrib import admin

from .models import TWorker
from datetime import datetime
import time

from .base_update import update

def make_tworker(modeladmin, request, queryset):
    b = TWorker(date_start=datetime.now())
    b.yes_processed_rows, b.not_processed_rows, b.log_text = update()
    b.date_end=datetime.now()
    b.save()
make_tworker.short_description = "Обновление базы"

class TWorkerAdmin(admin.ModelAdmin):
    # fields = (('papnum'), ('name', 'prename'), ('titul_image'), 'comment')
    list_display = ('id', 'date_start', 'date_end', 'yes_processed_rows', 'not_processed_rows')
    actions = [make_tworker]
    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'make_tworker':
            if not request.POST.getlist(admin.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                for u in TWorker.objects.all():
                    post.update({admin.ACTION_CHECKBOX_NAME: str(u.id)})
                request._set_post(post)
        return super(TWorkerAdmin, self).changelist_view(request, extra_context)

admin.site.register(TWorker, TWorkerAdmin)