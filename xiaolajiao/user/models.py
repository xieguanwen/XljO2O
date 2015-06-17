# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.contrib.auth.hashers import make_password

class passwordCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        pass


class User(models.Model):
    RANK = ((1,"代理商"),(2,"店铺"))
    userId = models.AutoField("会员编号",primary_key=True)
    userName = models.CharField("会员名称",max_length=50)
    password = models.CharField("密码",max_length=128)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    rank = models.SmallIntegerField("等级",choices=RANK,default=RANK[0][0])
    email = models.CharField("电子邮件",max_length=50,blank=True)
    sex = models.CharField("性别",max_length=10,blank=True)
    integration = models.IntegerField("积分",default=0,blank=True)
    lastLogin = models.DateTimeField("最后登录时间",blank=True)
    visitCount = models.IntegerField("登录次数",blank=True)
    mobile = models.CharField("手机",max_length=18,unique=True)
    tel = models.CharField("电话",max_length=20,blank=True)
    agentsId = models.IntegerField('代理商编号',blank=True,editable=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __unicode__(self):
        return self.userName

    class Meta():
        db_table = "user"
        app_label = "user"
        verbose_name = "会员"
        verbose_name_plural = "会员"



    




