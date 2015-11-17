import datetime
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from xiaolajiao.agents.models import Agents
from django.db import connection

def batchsncode(request):
    content = {}
    content.update(csrf(request))
    agentses = Agents.objects.all()
    content.update({"agentses":agentses})
    if(request.POST):
        if(int(request.POST['agentsId']) == 0):
            content.update({"errorMessage":"not select agents"})
            return render_to_response("sncode/batch_add.html",content)
        file_obj = request.FILES['uploadBatchAdd']
        # print(file_obj.name.split('.')[1])
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
                sql = """ insert INTO sn_code(imei, agentsId, status, addTime) VALUES (%s,%s,%s,%s) """
                param = [row[0],request.POST['agentsId'],0,datetime.datetime.now()]
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
