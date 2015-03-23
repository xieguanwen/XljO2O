# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from stores.models import Clerk

class Comment(models.Model):
    commentId = models.AutoField("",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")
    subject = models.CharField("主题",max_length=100)
    star = models.SmallIntegerField("分数")
    content = models.TextField("评论内容")
    user_id = models.IntegerField("官网用户")
    commenterMobile = models.CharField("评论手机",max_length=20)
    imei = models.CharField("IMEI码",max_length=20)

    def __unicode__(self):
        return self.subject

    class Meta:
        db_table = "comment"
        app_label = "comment"
        verbose_name = "评论"
        verbose_name_plural = "评论"
