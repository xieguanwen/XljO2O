# -*- coding: utf-8 -*-
from django.db import models

class Region(models.Model):
    TYPE = ((0,"国家"),(1,"省"),(2,"市"),(3,"地区"))
    regionId = models.AutoField("编号",primary_key=True)
    parentId = models.ForeignKey("self",db_column="regionId",verbose_name="父类编号")
    name = models.CharField("名称",max_length=50)
    type = models.SmallIntegerField("类型",default=TYPE[3][0],choices=TYPE)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "region"
        app_label = "region"
        verbose_name = "地区"
        verbose_name_plural = "地区"





