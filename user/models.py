# -*- coding: utf-8 -*-
import datetime
from django.db import models

class User(models.Model):
    RANK = ((1,"店铺"),(2,"代理商"))
    userId = models.AutoField("用户编号",primary_key=True)
    userName = models.CharField("用户名称",max_length=50)
    password = models.CharField("密码",max_length=32)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    rank = models.SmallIntegerField("等级",choices=RANK,default=RANK[0][0])
    email = models.CharField("电子邮件",max_length=50)
    sex = models.CharField("性别",max_length=10,blank=True)
    integration = models.IntegerField("积分",default=0,blank=True)
    lastLogin = models.DateTimeField("最后登录时间",blank=True)
    visitCount = models.IntegerField("登录次数",blank=True)
    mobile = models.CharField("手机",max_length=18)
    tel = models.CharField("电话",max_length=20,blank=True)

    def __unicode__(self):
        return self.userName


    class Meta():
        db_table = "user"
        app_label = "user"
        verbose_name = "用户"
        verbose_name_plural = "用户"



    




