from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'generic_app.views.generic_app_view', name='generic_app')
)
