# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from stores.models import Clerk

class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Store,db_column="id")
    user_id = models.IntegerField()
    favoriteMobile = models.CharField(max_length=20)
    clerkId = models.ForeignKey(Clerk,db_column="id")

    def __unicode__(self):
        return self.favoriteMobile

    class Meta:
        db_table = "favorite"
        app_label = "favorite"



