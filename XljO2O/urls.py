from django.conf.urls import patterns, include, url
from xiaolajiao.statistics import urls as statisticsUrls
# Uncomment the next two lines to enable the admin:
import xadmin

# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = patterns('',
    url(r'^', include(xadmin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^statistics/', include(statisticsUrls)),
    # url(r'^api/',include('api.urls')),
)

