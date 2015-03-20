# -*- coding: utf-8 -*-
import datetime
from django.db import models
from agents.models import Agents
from region.models import Region

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    agentsId = models.ForeignKey(Agents,db_column="id")
    storeName = models.CharField(max_length=150)
    province = models.ForeignKey(Region,db_column="id")
    city = models.ForeignKey(Region,db_column="id")
    region = models.ForeignKey(Region,db_column="id")
    street = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    introduce = models.CharField(max_length=20)
    license = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    storePicture = models.CharField(max_length=100)
    mainPicture = models.CharField(max_length=100)
    addTime = models.DateTimeField(default=datetime.datetime.now())
    status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.storeName

    class Meta:
        db_table = "store"
        app_label = "stores"


class Clerk(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    storeId = models.ForeignKey(Store,db_column="id")
    sex = models.CharField(max_length=10)
    constellation = models.CharField(max_length=15)
    addTime = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "clerk"
        app_label = "stores"