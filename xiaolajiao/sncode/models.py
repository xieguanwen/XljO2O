# -*- coding: utf-8 -*-
from django.db import models
from xiaolajiao.agents.models import Agents
from xiaolajiao.agents.models import MultiAgents
from xiaolajiao.stores.models import Store
import datetime

class SnCode(models.Model):
    SNCODE_STATUS = ((0,"未用"),(1,"已用"),(2,"退货"))
    imei = models.BigIntegerField("IMEI",unique=True,primary_key=True)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    status = models.SmallIntegerField("串码状态",choices=SNCODE_STATUS,default=SNCODE_STATUS[0][0])
    addTime = models.DateTimeField("增加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.imei)

    class Meta():
        db_table = 'sn_code'
        app_label = 'sncode'
        verbose_name = "串码"
        verbose_name_plural = "串码"

def getStoreId():
    return Store.objects.get(storeId=1)

class SnCodeAgents(models.Model):
    imei = models.BigIntegerField("IMEI",unique=True,primary_key=True)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    multiAgentsId = models.ForeignKey(MultiAgents,db_column="multiAgentsId",verbose_name="地包")
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺",blank=True,null=True)
    addTime = models.DateTimeField("增加时间",default=datetime.datetime.now())


    def __unicode__(self):
        return unicode(self.imei)

    class Meta():
        db_table = 'sn_code_agents'
        app_label = 'sncode'
        verbose_name = "代理商串码"
        verbose_name_plural = "代理商串码"

