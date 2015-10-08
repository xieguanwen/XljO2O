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
    agentsNo = models.IntegerField('代理商维一编号',help_text="例如：只能用数字",blank=True,default=int(time.time()))


    def __unicode__(self):
        return unicode(self.companyName)

    class Meta:
        db_table = "agents"
        app_label = "agents"
        verbose_name = "代理商"
        verbose_name_plural = "代理商"
    




