# -*- coding: utf-8 -*-
import datetime
from django.db import models
from user.models import User

class Agents(models.Model):
    agentsId = models.AutoField("代理商编号",primary_key=True)
    userId = models.ForeignKey(User,db_column="userId",verbose_name="用户名")
    companyName = models.CharField("公司名称",max_length=50)
    license = models.FileField("营业执照",upload_to="../images/uploads/")
    certificate = models.FileField("授权证书",upload_to="../images/uploads/")
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.companyName

    class Meta:
        db_table = "agents"
        app_label = "agents"
        verbose_name = "代理商"
        verbose_name_plural = "代理商"
    




