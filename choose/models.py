# -*- coding: utf-8 -*-
from django.db import models
from stores.models import Store
from stores.models import Clerk

class SelectedTheme(models.Model):
    selectedThemeId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    period = models.IntegerField()
    type = models.SmallIntegerField()

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "selected_theme"
        app_label = "choose"

class StoreAward(models.Model):
    storeAwardId = models.AutoField(primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId")
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="selectedThemeId")
    overallScore = models.IntegerField()

    def __unicode__(self):
        return self.selectedThemeId

    class Meta:
        db_table = "store_award"
        app_label = "choose"

class ClerkAward(models.Model):
    id = models.AutoField(primary_key=True)
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="selectedThemeId")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId")
    overallScore = models.IntegerField()

    def __unicode__(self):
        return self.clerkId

    class Meta:
        db_table = "clerk_award"
        app_label = "choose"