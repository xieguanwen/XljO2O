# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from stores.models import Clerk

class SelectedTheme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    period = models.IntegerField()
    type = models.SmallIntegerField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "selectedTheme"
        app_label = "choose"

class StoreAward(models.Model):
    id = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Store,db_column="id")
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="id")
    overallScore = models.IntegerField()

    def __unicode__(self):
        return self.selectedThemeId

    class Meta:
        db_table = "storeAward"
        app_label = "choose"

class ClerkAward(models.Model):
    id = models.AutoField(primary_key=True)
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="id")
    clerkId = models.ForeignKey(Clerk,db_column="id")
    overallScore = models.IntegerField()

    def __unicode__(self):
        return self.clerkId

    class Meta:
        db_table = "clerkAward"
        app_label = "choose"