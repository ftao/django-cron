from threading import Timer
import datetime
from django.http import HttpResponse
from django.conf import settings
from django_cron.base import cronScheduler
from django_cron.models import Cron,Job

#TODO change the name
polling_frequency = getattr(settings, "CRON_POLLING_FREQUENCY", 300)

def run_cron(request):
    Timer(2, cronScheduler.execute).start()
    return HttpResponse('cron is running')


def reset(request):
    status, created = Cron.objects.get_or_create(pk=1)
    #may be in bad state
    if (status.executing and
        status.last_run + datetime.timedelta(seconds=polling_frequency) < datetime.datetime.now()):
        status.executing = False
        status.save()
        return HttpResponse('cron status is reseted')
    else:
        return HttpResponse('cron status is normal')

        
