from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'apps.static.views.index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
