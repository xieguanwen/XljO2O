# -*- coding: utf-8 -*-
import datetime
from django.db import models
from agents.models import Agents
from region.models import Region

class Store(models.Model):
    storeId = models.AutoField("店铺编号",primary_key=True)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理")
    storeName = models.CharField("门店名称",max_length=150)
    # province = models.ManyToOneRel(Region)
    # city = models.ManyToOneRel(Region)
    # region = models.ManyToOneRel(Region)
    province = models.IntegerField("省")
    city = models.IntegerField("市")
    region = models.IntegerField("地区")
    street = models.CharField("街道",max_length=200)
    address = models.CharField("地址",max_length=255)
    tel = models.CharField("电话",max_length=20)
    contact = models.CharField("联系人",max_length=20)
    introduce = models.CharField("介绍",max_length=20)
    license = models.FileField("营业执照",upload_to="./images/uploads/")
    certificate = models.FileField("授权证书",upload_to="./images/uploads/")
    storePicture = models.FileField("门面图片",upload_to="./images/uploads/")
    mainPicture = models.FileField("主展区图片",upload_to="./images/uploads/")
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    status = models.SmallIntegerField("状态",default=0,help_text="店铺状态 0：审核中，1：营业中，2：已停业")

    def __unicode__(self):
        return self.storeName

    class Meta:
        db_table = "store"
        app_label = "stores"
        verbose_name = "店铺"
        verbose_name_plural = "店铺"


class Clerk(models.Model):
    clerkId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名字",max_length=50)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    sex = models.CharField("性别",max_length=10)
    constellation = models.CharField("星座",max_length=15)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "clerk"
        app_label = "stores"
        verbose_name = "店员"
        verbose_name_plural = "店员"