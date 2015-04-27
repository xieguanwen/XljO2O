# -*- coding: utf-8 -*-
import datetime

from django.db import models

from xiaolajiao.user.models import User


class Agents(models.Model):
    agentsId = models.AutoField("代理商编号",primary_key=True)
    userId = models.ForeignKey(User,db_column="userId",verbose_name="用户名")
    agentsRegion = models.CharField("代理商省区",max_length=50,help_text="例如：北京。也可以用多个")
    contact = models.CharField("联系人",max_length=50)
    companyName = models.CharField("公司名称",max_length=50)
    license = models.FileField("营业执照",upload_to="./images/uploads/")
    certificate = models.FileField("授权证书",upload_to="./images/uploads/")
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    tel = models.CharField("电话",max_length=30,blank=True)
    status = models.SmallIntegerField('状态',help_text="0:未通过,1:通过",default=0,blank=True)
    agentsRegion = models.CharField('代理地区',max_length=50,blank=True)
    agentsNo = models.IntegerField('代理商维一编号',help_text="例如：只能用数字")


    def __unicode__(self):
        return self.companyName

    class Meta:
        db_table = "agents"
        app_label = "agents"
        verbose_name = "代理商"
        verbose_name_plural = "代理商"
    




