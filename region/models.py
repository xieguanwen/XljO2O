# -*- coding: utf-8 -*-
from django.db import models

class Region(models.Model):
    regionId = models.AutoField("编号",primary_key=True)
    parentId = models.IntegerField("父亲编号")
    name = models.CharField("名称",max_length=50)
    type = models.SmallIntegerField("类型")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "region"
        app_label = "region"
        verbose_name = "地区"
        verbose_name_plural = "地区"





