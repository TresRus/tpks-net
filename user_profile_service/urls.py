__author__ = 'bohulenkov14'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('user_profile_service.views',
    url(r'^(?P<user_id>\d+)/$', 'detail'),
)
