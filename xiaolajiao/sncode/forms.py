# -*- coding: utf-8 -*-
from django import forms
from xiaolajiao.sncode.models import SnCodeAgents
# import threading
# import time

# def worker(objSCA):
#     print '##################################'
#     print objSCA.imei
#     time.sleep(8)
#     from django.db import connection
#     cursor = connection.cursor()
#     # cursor.execute("UPDATE sn_code_agents SET storeId = 0 WHERE imei = %s", [objSCA.imei])
#     cursor.execute("select storeId from sn_code_agents WHERE imei = %s", [objSCA.imei])
#     print cursor.fetchone()
#     return

class SnCodeAgentsChangeForm(forms.ModelForm):
    # field modify

    class Meta:
        Model = SnCodeAgents

    def save(self, commit=True):
        objSCA = super(SnCodeAgentsChangeForm, self).save(commit=False)
        if(commit):
            objSCA.save()

        return objSCA

