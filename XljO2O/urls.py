from django.conf.urls import patterns, include, url

import xadmin
xadmin.autodiscover()

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(xadmin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^statistics/', include('xiaolajiao.statistics.urls')),
    # url(r'^api/',include('api.urls')),
)
