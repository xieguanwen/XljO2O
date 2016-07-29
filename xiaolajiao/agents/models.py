# -*- coding: utf-8 -*-
import datetime
import time
from django.db import models
from xiaolajiao.user.models import User


class Agents(models.Model):
    STATUS = ((0,"未通过"),(1,"通过"))
    agentsId = models.AutoField("代理商编号",primary_key=True)
    userId = models.ForeignKey(User,db_column="userId",verbose_name="会员名")
    contact = models.CharField("联系人",max_length=50,blank=True)
    companyName = models.CharField("公司名称",max_length=50)
    license = models.FileField("营业执照",upload_to="./images/uploads/",blank=True)
    certificate = models.FileField("授权证书",upload_to="./images/uploads/",blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    tel = models.CharField("电话",max_length=30,blank=True)
    status = models.SmallIntegerField('状态',help_text="0:未通过,1:通过",choices=STATUS,default=STATUS[0][0],blank=True)
    agentsRegion = models.CharField('代理地区',max_length=50,blank=True,help_text="例如：北京。也可以用多个")
    agentsNo = models.IntegerField('代理商维一编号',help_text="例如：只能用数字",blank=True,default=int(time.time()),unique=True)

    def __unicode__(self):
        return unicode(self.companyName)

    class Meta:
        db_table = "agents"
        app_label = "agents"
        verbose_name = "代理商"
        verbose_name_plural = "代理商"

class MultiAgents(models.Model):
    STATUS = ((0,"未通过"),(1,"通过"))
    multiAgentsId = models.AutoField("地包",primary_key=True)
    name = models.CharField("地包名",max_length=50)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    multiAgentsNo = models.IntegerField("地包代号",blank=True)
    userId = models.ForeignKey(User,db_column="userId",verbose_name="用户")
    status = models.SmallIntegerField("状态",default=STATUS[0][0],choices=STATUS,help_text="0:未通过,1:通过")
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    contact = models.CharField("联系人",max_length=50,blank=True)
    contactTel = models.CharField("联系人电话",max_length=18,blank=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta():
        db_table = "multi_agents"
        app_label = "agents"
        verbose_name = "地包"
        verbose_name_plural = "地包"

class Supervise(models.Model):
    superviseId = models.AutoField("督导",primary_key=True)
    name = models.CharField("督导名字",max_length=50)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    tel = models.CharField("电话号码",max_length=50)
    mobile = models.CharField("手机",max_length=50)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    multiAgentsId = models.ForeignKey(MultiAgents,db_column="multiAgentsId",verbose_name="地包",blank=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta():
        db_table = "supervise"
        app_label = "agents"
        verbose_name = "督导"
        verbose_name_plural = "督导"