# -*- coding: utf-8 -*-
import datetime
from django.db import models

class User(models.Model):
    userId = models.AutoField("用户编号",primary_key=True)
    userName = models.CharField("用户名称",max_length=50)
    password = models.CharField("密码",max_length=32)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    rank = models.SmallIntegerField("等级",default=(1,2))
    email = models.CharField("电子邮件",max_length=50)
    sex = models.CharField("性别",max_length=10)
    integration = models.IntegerField("积分",default=0,blank=True)
    lastLogin = models.DateTimeField("最后登录时间",blank=True)
    visitCount = models.IntegerField("登录次数")
    mobile = models.CharField("手机",max_length=18)
    tel = models.CharField("电话",max_length=20)

    def __unicode__(self):
        return self.userName

    class Meta():
        db_table = "user"
        app_label = "user"



    




