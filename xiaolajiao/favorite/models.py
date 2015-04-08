# -*- coding: utf-8 -*-
from django.db import models

from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk


class Favorite(models.Model):
    favoriteId = models.AutoField("编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    user_id = models.IntegerField("官网用户")
    favoriteMobile = models.CharField("点赞手机",max_length=20)
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")

    def __unicode__(self):
        return self.favoriteMobile

    class Meta:
        db_table = "favorite"
        app_label = "favorite"
        verbose_name = "点赞"
        verbose_name_plural = "点赞"



