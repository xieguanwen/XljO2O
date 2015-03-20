# -*- coding: utf-8 -*-
import datetime
from django.db import models

class User(models.Model):
    id = models.AutoField(u"会员编号",primary_key=True)
    userName = models.CharField(u"会员名称",max_length=50)
    password = models.CharField(u"密码",max_length=32)
    addTime = models.DateTimeField(u"增加时间",default=datetime.datetime.now())
    rank = models.SmallIntegerField(u"会员等级",default=(1,2))
    email = models.CharField(u"电子邮件",max_length=50)
    sex = models.CharField(u"性别",max_length=10)
    integration = models.IntegerField(u"积分",default=0,blank=True)
    lastLogin = models.DateTimeField(u"最后登录时间",blank=True)
    visitCount = models.IntegerField(u"登录次数")
    mobile = models.CharField(u"手机号码")
    tel = models.CharField(u"电话号码")

    def __unicode__(self):
        return self.userName

    class Meta():
        db_table = "user"
        app_label = "Member"


    




