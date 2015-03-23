# -*- coding: utf-8 -*-
from django.db import models

class Region(models.Model):
    regionId = models.AutoField(primary_key=True)
    parentId = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.SmallIntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "region"
        app_label = "region"





