# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('dnsalloc.views',
    (r'^$', 'show_home'),
    (r'^dashboard/$', 'show_dashboard'),
    (r'^dashboard/service/create/$', 'create_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/$', 'show_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/edit/$', 'edit_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/switch/$', 'switch_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/force/$', 'force_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/delete/$', 'delete_service'),
    (r'^dashboard/service/(?P<service_id>\d+)/delete/ask/$', 'delete_service_ask'),
    (r'^feed/service/(?P<service_id>\d+)/status/$', 'feed_service'),
)
