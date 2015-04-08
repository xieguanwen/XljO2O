from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'api/views',
    (r'^api/$','index'),
)