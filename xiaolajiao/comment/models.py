# -*- coding: utf-8 -*-
import datetime
from django.db import models
from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk


class ActiveComment(models.Model):
    activeCommentId = models.AutoField("活动评论编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    subject = models.CharField("主题",max_length=100)
    star = models.SmallIntegerField("分数")
    content = models.TextField("评论内容")
    user_id = models.IntegerField("官网用户")
    # commenterMobile = models.CharField("评论手机",max_length=20)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = "active_comment"
        app_label = "comment"
        verbose_name = "活动评论"
        verbose_name_plural = "活动评论"

class StoreComment(models.Model):
    STATUS = ((0,"未审核"),(1,"已审核"))
    storeCommentId = models.AutoField("店铺评论编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")
    subject = models.CharField("主题",max_length=100,blank=True)
    star = models.SmallIntegerField("分数")
    content = models.TextField("评论内容")
    user_id = models.IntegerField("官网用户")
    commenterMobile = models.CharField("评论手机",max_length=20,blank=True)
    imei = models.CharField("IMEI码",max_length=20,blank=True)
    addTime = models.DateTimeField("添加时间",default=datetime.datetime.now())
    status = models.SmallIntegerField("状态",default=STATUS[0][0],choices=STATUS,help_text="0:没有核对，1:已经核对")

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = "store_comment"
        app_label = "comment"
        verbose_name = "店铺评论"
        verbose_name_plural = "店铺评论"
