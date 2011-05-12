from django.conf.urls.defaults import *
from django_cron.views import run_cron,reset

urlpatterns = patterns('',
   url(r'^run/$', run_cron),
   url(r'^reset/$', reset),
)


