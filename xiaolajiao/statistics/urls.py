import views
from django.conf.urls import url

urlpatterns = [
    url('^index[/]$',views.index,name="index"),
    url('^downloadcsv$',views.downloadcsv,name="downloadcsv"),
    url('^agents$',views.agents,name="agents"),
]


