# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from stores.models import Clerk

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Store,db_column="id")
    clerkId = models.ForeignKey(Clerk,db_column="id")
    subject = models.CharField(max_length=100)
    star = models.SmallIntegerField()
    content = models.TextField()
    user_id = models.IntegerField()
    commenterMobile = models.CharField(max_length=20)
    imei = models.CharField(max_length=20)

    def __unicode__(self):
        return self.subject

    class Meta:
        db_table = "comment"
        app_label = "comment"
