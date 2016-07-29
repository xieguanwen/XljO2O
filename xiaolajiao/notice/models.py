# -*- coding: utf-8 -*-
from django.db import models

class NoticeCat(models.Model):
    noticeCatId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名称",max_length=100)
    type = models.SmallIntegerField("类型")
    contentTemplate = models.TextField("模板")

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = "notice_cat"
        app_label = "notice"
        verbose_name = "通知分类"
        verbose_name_plural = "通知分类"

class Notice(models.Model):
    noticeId = models.AutoField("编号",primary_key=True)
    subject = models.CharField("标题",max_length=255)
    content = models.TextField("内容")
    noticeCatId = models.ForeignKey(NoticeCat,db_column="noticeCatId",verbose_name="通知分类")

    def __unicode__(self):
        return unicode(self.subject)

    class Meta:
        db_table = "notice"
        app_label = "notice"
        verbose_name = "通知"
        verbose_name_plural = "通知"
