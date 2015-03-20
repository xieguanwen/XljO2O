# -*- coding: utf-8 -*-
from django.db import models

class NoticeCat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.SmallIntegerField()
    contentTemplate = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "noticeCat"
        app_label = "notice"

class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    noticeCatId = models.ForeignKey(NoticeCat,db_column="id")

    def __unicode__(self):
        return self.subject

    class Meta:
        db_table = "notice"
        app_label = "notice"
