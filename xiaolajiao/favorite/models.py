# -*- coding: utf-8 -*-
import datetime
from django.db import models
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk
from xiaolajiao.active.models import Active

class Favorite(models.Model):
    clerkFavoriteId = models.AutoField("编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    user_id = models.IntegerField("官网用户")
    favoriteMobile = models.CharField("点赞手机",max_length=20)
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")

    def __unicode__(self):
        return self.favoriteMobile

    class Meta:
        db_table = "clerk_favorite"
        app_label = "favorite"
        verbose_name = "店员点赞"
        verbose_name_plural = "店员点赞"

class ActiveFavorite(models.Model):
    activeFavoriteId = models.AutoField("编号",primary_key=True)
    activeId = models.ForeignKey(Active,db_column="activeId",verbose_name="活动编号")
    user_id = models.IntegerField("官网用户")
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    total = models.IntegerField("总数",default=0,blank=True)
    addTime = models.DateTimeField("添增时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.activeId

    class Meta:
        db_table = "active_favorite"
        app_label = "favorite"
        verbose_name = "活动点赞"
        verbose_name_plural = "活动点赞"