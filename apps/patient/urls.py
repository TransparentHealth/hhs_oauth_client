from __future__ import absolute_import
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .views import *


urlpatterns = patterns('',
    url(r'^cms/pull/me', bbof_pull_me,  name="bbof_pull_me"),

)
