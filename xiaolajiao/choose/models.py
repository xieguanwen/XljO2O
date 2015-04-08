# -*- coding: utf-8 -*-
from django.db import models

from xiaolajiao.stores.models import Store
from xiaolajiao.stores.models import Clerk


class SelectedTheme(models.Model):
    TYPE = ((1,"周"),(2,"月"),(3,"年"))
    selectedThemeId = models.AutoField("主题编号",primary_key=True)
    name = models.CharField("主题",max_length=200)
    period = models.IntegerField("周期数")
    type = models.SmallIntegerField("类型",choices=TYPE,default=TYPE[0][0],help_text="1：为周，2：为月，3：为年")

    def __unicode__(self):
        return self.name
    class Meta:
        db_table = "selected_theme"
        app_label = "choose"
        verbose_name = "评选主题"
        verbose_name_plural = "评选主题"

class StoreAward(models.Model):
    storeAwardId = models.AutoField("编号",primary_key=True)
    storeId = models.ForeignKey(Store,db_column="storeId",verbose_name="店铺")
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="selectedThemeId",verbose_name="主题")
    overallScore = models.IntegerField("综合分数")

    def __unicode__(self):
        return self.selectedThemeId

    class Meta:
        db_table = "store_award"
        app_label = "choose"
        verbose_name = "店铺评选"
        verbose_name_plural = "店铺评选"

class ClerkAward(models.Model):
    id = models.AutoField("编号",primary_key=True)
    selectedThemeId = models.ForeignKey(SelectedTheme,db_column="selectedThemeId",verbose_name="主题")
    clerkId = models.ForeignKey(Clerk,db_column="clerkId",verbose_name="店员")
    overallScore = models.IntegerField("综合分数")

    def __unicode__(self):
        return self.clerkId

    class Meta:
        db_table = "clerk_award"
        app_label = "choose"
        verbose_name = "店员评选"
        verbose_name_plural = "店员评选"