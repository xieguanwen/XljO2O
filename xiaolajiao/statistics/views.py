import datetime
import csv
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.db import connection
from models import StoreData
from django.http.response import HttpResponse

def index(request):
    data = {}
    data.update(csrf(request))
    if(request.POST):
        data.update(request.POST)
        endDate = request.POST['endDate']
        startDate = request.POST['startDate']
        # print(data.get('endDate')[0])
    else:
        startDate = datetime.date.today()
        endDate = startDate + datetime.timedelta(1)
    storeData = StoreData(startDate,endDate)
    data.setdefault('data',storeData.getStatistics())

    # endDate = datetime.date(2015,6,15)
    return render_to_response('xiaolajiao/statistics/index.html',data)

def downloadcsv(request):
    # startDate = request.GET['startDate']
    # endDate = request.GET['endDate']
    startDate = '2015/05/04'
    endDate = '2015/05/05'
    storeData = StoreData(startDate,endDate)
    response = HttpResponse("text csv")
    response['Content-Disposition'] = 'attachment; filename=1212.csv'
    fieldnames = ['province','provinceName','numberOfCity','numberOfTowns','numberOfStores','newStores','newCity','newTown']
    dictWriter = csv.DictWriter(response,fieldnames)
    rows = storeData.getStatistics()
    print(rows)
    dictWriter.writerow(fieldnames)
    dictWriter.writerows(rows)
    return response