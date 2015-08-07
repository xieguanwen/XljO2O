import datetime
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.db import connection
from models import StoreData

def index(request):
    data = {}
    data.update(csrf(request))
    if(request.POST):
        data.update(request.POST)
        endDate = request.POST['endDate']
        startDate = request.POST['startDate']
        print(data.get('endDate')[0])
    else:
        endDate = datetime.date.today()
    # storeData = StoreData(startDate,endDate)

    endDate = datetime.date(2015,6,15)

    # l = ()
    # l.__len__()
    # print(row.__len__())
    return render_to_response('xiaolajiao/statistics/index.html',data)

