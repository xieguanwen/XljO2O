# -*- coding: utf-8 -*-
import datetime
from django.db import models

class ECouponCat(models.Model):
    ECouponCatId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "e_coupon_cat"
        app_label = "coupon"

class ElectronicCoupons(models.Model):
    electronicCouponsId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    eCouponCatId = models.ForeignKey(ECouponCat,db_column="eCouponCatId")
    code = models.CharField(max_length=50)
    startTime = models.DateTimeField(default=datetime.datetime.now())
    endTime = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "electronic_coupons"
        app_label = "coupon"

