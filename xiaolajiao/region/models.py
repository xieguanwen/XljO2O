# -*- coding: utf-8 -*-
from django.db import models


class Province(models.Model):
    TYPE = ((0,"国家"),(1,"省"),(2,"市"),(3,"地区"))
    region_id = models.AutoField("编号",primary_key=True)
    parent_id = models.IntegerField("父类编号",default=0)
    region_name = models.CharField("名称",max_length=50)
    region_type = models.SmallIntegerField("类型",default=TYPE[3][0],choices=TYPE)
    agency_id = models.SmallIntegerField("没有作用",blank=True,editable=False)

    def __unicode__(self):
        return self.region_name

    class Meta:
        db_table = "province"
        app_label = "region"
        verbose_name = "地区"
        verbose_name_plural = "地区"


class City(models.Model):
    TYPE = ((0,"国家"),(1,"省"),(2,"市"),(3,"地区"))
    region_id = models.AutoField("编号",primary_key=True)
    parent_id = models.ForeignKey(Province,db_column="region_id",verbose_name="父类编号")
    region_name = models.CharField("名称",max_length=50)
    region_type = models.SmallIntegerField("类型",default=TYPE[3][0],choices=TYPE)
    agency_id = models.SmallIntegerField("没有作用",blank=True,editable=False)

    def __unicode__(self):
        return self.region_name

    class Meta:
        db_table = "city"
        app_label = "region"
        verbose_name = "地区"
        verbose_name_plural = "地区"


class Region(models.Model):
    TYPE = ((0,"国家"),(1,"省"),(2,"市"),(3,"地区"))
    region_id = models.AutoField("编号",primary_key=True)
    parent_id = models.ForeignKey(City,db_column="region_id",verbose_name="父类编号")
    region_name = models.CharField("名称",max_length=50)
    region_type = models.SmallIntegerField("类型",default=TYPE[3][0],choices=TYPE)
    agency_id = models.SmallIntegerField("没有作用",blank=True,editable=False)

    def __unicode__(self):
        return self.region_name

    class Meta:
        db_table = "region"
        app_label = "region"
        verbose_name = "地区"
        verbose_name_plural = "地区"




