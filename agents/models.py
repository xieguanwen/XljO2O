# -*- coding: utf-8 -*-
import datetime
from django.db import models
from user.models import User

class Agents(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User,db_column="id")
    companyName = models.CharField(max_length=50)
    license = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    addTime = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.companyName

    class Meta:
        db_table = "agents"
        app_label = "agents"
    




