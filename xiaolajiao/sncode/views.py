import datetime
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from xiaolajiao.sncode.models import SnCode
from django.db import connection

def batchsncode(request):
    content = {}
    content.update(csrf(request))
    if(request.POST):
        file_obj = request.FILES['uploadBatchAdd']
        print(file_obj.name.split('.')[1])
        if(file_obj.name.split('.')[1] == "csv"):
            import csv
            import StringIO
            buf = StringIO.StringIO(file_obj.read())
            try:
                reader = csv.reader(buf)
            except:
                content.update({"errorMessage":"error csv"})
                return render_to_response("sncode/batch_add.html",content)

            cursor = connection.cursor()
            successCount = 0
            faultCount = 0
            for row in reader:
                print(row[1])
                if(len(row)!=3):
                    continue
                sql = """ insert INTO sn_code(imei, agentsId, status, addTime) VALUES (%s,%s,%s,%s) """
                param = [row[0],row[1],row[2],datetime.datetime.now()]
                try:
                    cursor.execute(sql,param)
                    successCount = successCount + 1
                except:
                    faultCount = faultCount + 1
            cursor.close()
            content.update({"batchUploadSuccess":1,"successCount":successCount,"faultCount":faultCount})
    return render_to_response("sncode/batch_add.html",content)

def handle_uploaded_file(fileOject, path = './'):
    destination = open(path + fileOject.name, 'wb+')
    for chunk in fileOject.chunks():
        destination.write(chunk)
    destination.close()
