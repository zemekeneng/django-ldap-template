from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^accounts/', include('accounts.urls')),
    url(r'^generic_app/', include('generic_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
