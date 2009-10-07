from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'privatebeta.views.invite', name='privatebeta_invite'),
    url(r'^sent/$', 'privatebeta.views.sent', name='privatebeta_sent'),
)
