import datetime
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from xiaolajiao.agents.models import Agents
from django.db import connection
from django.utils.translation import ugettext as _

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
        cursor = connection.cursor()
        if(file_obj.name.split('.')[1] == "csv"):
            import csv
            import StringIO
            buf = StringIO.StringIO(file_obj.read())
            try:
                reader = csv.reader(buf)
            except:
                content.update({"errorMessage":_("error csv")})
                return render_to_response("sncode/batch_add.html",content)

            successCount = 0
            faultCount = 0
            for row in reader:
                if(len((row[0]))>=15 and len(row[0])<=20):
                    sql = """ insert INTO sn_code(imei, agentsId, status, addTime) VALUES (%s,%s,%s,%s) """
                    param = [row[0],request.POST['agentsId'],0,datetime.datetime.now()]
                    try:
                        cursor.execute(sql,param)
                        successCount = successCount + 1
                    except:
                        faultCount = faultCount + 1
                else:
                    content.update({"errorMessage":_("length is not 15 bit")})
                    return render_to_response("sncode/batch_add.html",content)
        elif(file_obj.name.split('.')[1] == "txt"):
            lines = file_obj.readlines()
            for line in lines:
                if(len(line)>=15 and len(line)<=20):
                    sql = """ insert INTO sn_code(imei, agentsId, status, addTime) VALUES (%s,%s,%s,%s) """
                    param = [line,request.POST['agentsId'],0,datetime.datetime.now()]
                    try:
                        cursor.execute(sql,param)
                        successCount = successCount + 1
                    except:
                        faultCount = faultCount + 1
                else:
                    content.update({"errorMessage":_("length is not 15 bit")})
                    return render_to_response("sncode/batch_add.html",content)
        cursor.close()
        content.update({"batchUploadSuccess":1,"successCount":successCount,"faultCount":faultCount})
    return render_to_response("sncode/batch_add.html",content)

def handle_uploaded_file(fileOject, path = './'):
    destination = open(path + fileOject.name, 'wb+')
    for chunk in fileOject.chunks():
        destination.write(chunk)
    destination.close()
