# -*- coding: Utf-8 -*-
import datetime
from django.db import models
from stores.models import Store

class ActiveTemplate(models.Model):
    activeTemplateId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    fileName = models.CharField(max_length=50)
    dirPath = models.CharField(max_length=100)
    series = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta():
        db_table = "active_template"
        app_label = "active"

class Active(models.Model):
    activeId = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId")
    subject = models.CharField(max_length=200)
    startTime = models.DateTimeField(default=datetime.datetime.now())
    endTime = models.DateTimeField(default=datetime.datetime.now())
    content = models.TextField()
    activeTemplateId = models.ForeignKey(ActiveTemplate,db_column="activeTemplateId")

    def __unicode__(self):
        return self.subject

    class Meta():
        db_table = "active"
        app_label = "active"

class ActiveTop(models.Model):
    activeTopId = models.AutoField(primary_key=True)
    activeId = models.ForeignKey(Active,db_column="id")
    sort = models.IntegerField()
    isDisplay = models.BooleanField()

    def __unicode__(self):
        return self.sort;

    class Meta:
        db_table = "active_top"
        app_label = "active"
