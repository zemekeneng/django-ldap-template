from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^login/', 'accounts.views.login_view', name='login'),
    url(r'^logout/', 'accounts.views.logout_view', name='logout'),
    url(r'^home/', 'accounts.views.loggedin_view', name='loggedin'),
    url(r'^auth/', 'accounts.views.auth_view', name='auth'),
    url(r'^invalid/', 'accounts.views.invalid_view', name='invalid'),
    # url(r'^register/', 'accounts.views.register_view', name='register'),
    # url(r'^register_success/', 'accounts.views.register_success_view',
    #      name='register_success'),

)
