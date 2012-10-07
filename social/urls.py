__author__ = 'bohulenkov14'
from django.conf.urls import patterns, include, url


urlpatterns = patterns('social.views',
    url(r'^$', 'login'),
)
