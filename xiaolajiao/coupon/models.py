# -*- coding: utf-8 -*-
import datetime
from django.db import models

class ECouponCat(models.Model):
    ECouponCatId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名称",max_length=200)
    type = models.SmallIntegerField("活动类型")

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = "e_coupon_cat"
        app_label = "coupon"
        verbose_name = "电子券分类"
        verbose_name_plural = "电子券分类"

class ElectronicCoupons(models.Model):
    electronicCouponsId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名称",max_length=50)
    eCouponCatId = models.ForeignKey(ECouponCat,db_column="eCouponCatId",verbose_name="电子券分类")
    code = models.CharField("电子券码",max_length=50)
    startTime = models.DateTimeField("开始时间",default=datetime.datetime.now())
    endTime = models.DateTimeField("结束时间",default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = "electronic_coupons"
        app_label = "coupon"
        verbose_name = "电子券"
        verbose_name_plural = "电子券"

