# -*- coding: utf-8 -*-
from django.db import models
from xiaolajiao.agents.models import Agents
from xiaolajiao.agents.models import MultiAgents
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk
import datetime
from xiaolajiao.region.models import Province
from xiaolajiao.region.models import City
from xiaolajiao.region.models import Region

class ProductType(models.Model):
    productTypeId = models.AutoField("产品类型",primary_key=True)
    tacCode = models.IntegerField("TAC")
    name = models.CharField("产品名称",max_length=100)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.name )

    class Meta():
        db_table = "product_type"
        app_label = "product"
        verbose_name = "产品类型"
        verbose_name_plural = "产品类型"

class ProductColor(models.Model):
    productColorId = models.AutoField("颜色编号",primary_key=True)
    colorValue = models.CharField("颜色值",max_length=100)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return unicode(self.colorValue)

    class Meta():
        db_table = "product_color"
        app_label = "product"
        verbose_name = "产品颜色"
        verbose_name_plural = "产品颜色"

class ProductSales(models.Model):
    productSalesId = models.AutoField("产品销售编号",primary_key=True)
    imei = models.CharField("IMEI",max_length=100)
    productModel = models.CharField("入网型号",max_length=100,blank=True)
    productName = models.CharField("设备名称",max_length=100)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理商")
    multiAgentsId = models.ForeignKey(MultiAgents,db_column="multiAgentsId",verbose_name="地包",blank=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员",blank=True)
    tacCode = models.CharField("TAC",max_length=100,blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    productColorId = models.ForeignKey(ProductColor,db_column="productColorId",verbose_name="产品颜色")
    province = models.ForeignKey(Province,db_column="province",verbose_name="省")
    city = models.ForeignKey(City,db_column="city",verbose_name="市")
    region = models.ForeignKey(Region,db_column="region",verbose_name="地区")

    def __unicode__(self):
        return unicode(self.productName)

    class Meta():
        db_table = "product_sales"
        app_label = "product"
        verbose_name = "产品销售"
        verbose_name_plural = "产品销售"
