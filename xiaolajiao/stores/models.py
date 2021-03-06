# -*- coding: utf-8 -*-
import datetime

from django.db import models
from xiaolajiao.agents.models import Agents
from xiaolajiao.agents.models import MultiAgents
from xiaolajiao.agents.models import Supervise
from xiaolajiao.user.models import User
from xiaolajiao.region.models import Region
from xiaolajiao.region.models import City
from xiaolajiao.region.models import Province


class Store(models.Model):
    STATUS = ((0,"审核中"),(1,"营业中"),(2,"已停业"))
    LOG_TYPE = ((0,"审请"),(1,"修改"))
    STORETYPE = ((0,"连锁门店"),(1,"独立门店"),(2,"综合门店"),(3,"营业厅店"))
    storeId = models.AutoField("店铺编号",primary_key=True)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理")
    userId = models.ForeignKey(User,db_column="userId",verbose_name="会员")
    storeName = models.CharField("门店名称",max_length=150)
    province = models.ForeignKey(Province,db_column="province",verbose_name="省")
    city = models.ForeignKey(City,db_column="city",verbose_name="市")
    region = models.ForeignKey(Region,db_column="region",verbose_name="地区")
    # province = models.IntegerField("省")
    # city = models.IntegerField("市")
    # region = models.IntegerField("地区")
    street = models.CharField("街道",max_length=200,blank=True)
    address = models.CharField("地址",max_length=255)
    tel = models.CharField("电话",max_length=20,blank=True)
    contact = models.CharField("联系人",max_length=20,blank=True)
    introduce = models.CharField("介绍",max_length=20,blank=True)
    license = models.FileField("营业执照",upload_to="./images/uploads/",blank=True)
    certificate = models.FileField("授权证书",upload_to="./images/uploads/",blank=True)
    storePicture = models.FileField("门面图片",upload_to="./images/uploads/",blank=True)
    mainPicture = models.TextField("主展区图片",blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    status = models.SmallIntegerField("状态",choices=STATUS,default=STATUS[0][0],help_text="店铺状态 0：审核中，1：营业中，2：已停业")
    longitude = models.CharField("经度", max_length=50, help_text="例如：120.73829749728",blank=True)
    latitude = models.CharField("纬度", max_length=50, help_text="例如：120.73829749728",blank=True)
    serviceTime = models.CharField("服务时间",max_length=100,help_text="例如：8:00-18:00",blank=True)
    getThere = models.TextField("服务时间",blank=True)
    logType = models.SmallIntegerField("日志类型",choices=LOG_TYPE,default=LOG_TYPE[0][0],help_text="0：申请,1：修改",editable=False)
    isOfficial = models.SmallIntegerField("是否官方",choices=((0,"非官方"),(1,"官方")),default=0)
    storeType = models.SmallIntegerField("店铺类型",choices=STORETYPE,default=STORETYPE[0][0])
    multiAgentsId = models.ForeignKey(MultiAgents,db_column="multiAgentsId",verbose_name="地包",blank=True)
    superviseId = models.ForeignKey(Supervise,db_column="superviseId",verbose_name="督导",blank=True,null=True)

    def __unicode__(self):
        return unicode(self.storeName)

    class Meta:
        db_table = "store"
        app_label = "stores"
        verbose_name = "店铺"
        verbose_name_plural = "店铺"


class StoreTemp(models.Model):
    STATUS = ((0,"审核中"),(1,"营业中"),(2,"已停业"))
    LOG_TYPE = ((0,"审请"),(1,"修改"))
    STORETYPE = ((0,"连锁门店"),(1,"独立门店"),(2,"综合门店"),(3,"营业厅店"))
    storeTempId = models.AutoField("店铺临时编号",primary_key=True)
    storeId = models.IntegerField("店铺编号",blank=True)
    agentsId = models.ForeignKey(Agents,db_column="agentsId",verbose_name="代理")
    userId = models.ForeignKey(User,db_column="userId",verbose_name="会员")
    storeName = models.CharField("门店名称",max_length=150)
    province = models.ForeignKey(Province,db_column="province",verbose_name="省")
    city = models.ForeignKey(City,db_column="city",verbose_name="市")
    region = models.ForeignKey(Region,db_column="region",verbose_name="地区",blank=True)
    street = models.CharField("街道",max_length=200,blank=True)
    address = models.CharField("地址",max_length=255)
    tel = models.CharField("电话",max_length=20,blank=True)
    contact = models.CharField("联系人",max_length=20,blank=True)
    introduce = models.CharField("介绍",max_length=20,blank=True)
    license = models.FileField("营业执照",upload_to="./images/uploads/",blank=True)
    certificate = models.FileField("授权证书",upload_to="./images/uploads/",blank=True)
    storePicture = models.FileField("门面图片",upload_to="./images/uploads/",blank=True)
    mainPicture = models.TextField("主展区图片",blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    status = models.SmallIntegerField("状态",choices=STATUS,default=STATUS[0][0],help_text="店铺状态 0：审核中，1：营业中，2：已停业")
    longitude = models.CharField("经度", max_length=50, help_text="例如：120.73829749728",blank=True)
    latitude = models.CharField("纬度", max_length=50, help_text="例如：120.73829749728",blank=True)
    serviceTime = models.CharField("服务时间",max_length=100,help_text="例如：8:00-18:00",blank=True)
    getThere = models.TextField("服务时间",blank=True)
    logType = models.SmallIntegerField("申请-修改",choices=LOG_TYPE,default=LOG_TYPE[0][0],help_text="0：申请,1：修改")
    isOfficial = models.SmallIntegerField("是否官方",choices=((0,"非官方"),(1,"官方")),default=0)
    storeType = models.SmallIntegerField("店铺类型",choices=STORETYPE,default=STORETYPE[0][0])
    multiAgentsId = models.ForeignKey(MultiAgents,db_column="multiAgentsId",verbose_name="地包",blank=True)
    superviseId = models.ForeignKey(Supervise,db_column="superviseId",verbose_name="督导",blank=True)

    def __unicode__(self):
        return unicode(self.storeName)

    class Meta:
        db_table = "store_temp"
        app_label = "stores"
        verbose_name = "审核店铺"
        verbose_name_plural = "审核店铺"



class Clerk(models.Model):
    SEX = (("男","男"),("女","女"))
    ISCELEBRITY = ((0,'否'),(1,'是'))
    CLERKTYPE = ((0,"店员"),(1,"促销员"))
    clerkId = models.AutoField("编号",primary_key=True)
    name = models.CharField("名字",max_length=50)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    sex = models.CharField("性别",max_length=10,blank=True,choices=SEX,default="男")
    constellation = models.CharField("星座",max_length=15,blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    isCelebrity = models.SmallIntegerField("明星店员",default=ISCELEBRITY[0][0],choices=ISCELEBRITY)
    photo = models.FileField("店员相片",upload_to="./images/uploads/",blank=True)
    slogan = models.CharField("店员口号",max_length=255)
    clerkType = models.SmallIntegerField("职员类型",choices=CLERKTYPE,default=CLERKTYPE[0][0])

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = "clerk"
        app_label = "stores"
        verbose_name = "店员"
        verbose_name_plural = "店员"