# -*- coding: Utf-8 -*-
import datetime
from django.db import models
from xiaolajiao.stores.models import Store
from ckeditor.fields import RichTextField


class ActiveTemplate(models.Model):
    activeTemplateId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名称",max_length=50)
    fileName = models.CharField("文件名",max_length=50)
    dirPath = models.CharField("显示目录",max_length=100)
    series = models.CharField("系列",max_length=100)

    def __unicode__(self):
        return self.name

    class Meta():
        db_table = "active_template"
        app_label = "active"
        verbose_name = "活动模板"
        verbose_name_plural = "活动模板"

class Active(models.Model):
    activeId = models.AutoField("编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    subject = models.CharField("主题",max_length=200)
    startTime = models.DateTimeField("开始时间",default=datetime.datetime.now(),blank=True)
    endTime = models.DateTimeField("结束时间",default=datetime.datetime.now(),blank=True)
    content = RichTextField("内容")
    # activeTemplateId = models.ForeignKey(ActiveTemplate,db_column="activeTemplateId",verbose_name="模板",blank=True)
    status = models.SmallIntegerField("状态",default=0,blank=True)
    rank = models.SmallIntegerField("重要性",default=0,help_text="0:表示一般等级,1:重要等级")
    sort = models.IntegerField("排序",default=0)
    isDisplay = models.SmallIntegerField("是显示",default=0,help_text="0:显示,1:不显示")
    visit = models.IntegerField("访问次数",default=0,blank=True)
    addTime = models.DateTimeField("添增时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.subject

    class Meta():
        db_table = "active"
        app_label = "active"
        verbose_name = "活动"
        verbose_name_plural = "活动"

class ActiveTop(models.Model):
    activeTopId = models.AutoField("编号",primary_key=True)
    activeId = models.ForeignKey(Active,db_column="id",verbose_name="活动")
    sort = models.IntegerField("排序")
    isDisplay = models.BooleanField("是否显示")

    def __unicode__(self):
        return self.sort;

    class Meta:
        db_table = "active_top"
        app_label = "active"
        verbose_name = "活动置顶"
        verbose_name_plural = "活动置顶"
