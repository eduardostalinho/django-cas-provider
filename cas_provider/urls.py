from django.conf.urls import patterns, url

from views import *

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^validate/', validate),
    url(r'^logout/', logout),
)
