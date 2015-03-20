# -*- coding: utf-8 -*-
import datetime
from django.db import models

class Member(models.Model):
    id = models.AutoField("会员编号",primary_key=True)
    userName = models.CharField("会员名称",max_length=50)
    password = models.CharField("密码",max_length=32)
    addTime = models.DateTimeField("增加时间",default=datetime.datetime.now())
    rank = models.SmallIntegerField("会员等级",default=(1,2))
    email = models.CharField("电子邮件",max_length=50)
    sex = models.CharField("性别",max_length=10)
    integration = models.IntegerField("积分",default=0,blank=True)
    lastLogin = models.DateTimeField("最后登录时间",blank=True)
    visitCount = models.IntegerField("登录次数")
    mobile = models.CharField("手机号码")
    tel = models.CharField("电话号码")

    def __unicode__(self):
        return self.userName

    class Meta():
        db_table = "user"
        app_label = "Member"


    




