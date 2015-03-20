# -*- coding: utf-8 -*-
import datetime
from django.db import models

class ECouponCat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "eCouponCat"
        app_label = "coupon"

class ElectronicCoupons(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    eCouponCatId = models.ForeignKey(ECouponCat,db_column="id")
    code = models.CharField(max_length=50)
    startTime = models.DateTimeField(default=datetime.datetime.now())
    endTime = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "electronicCoupons"
        app_label = "coupon"

