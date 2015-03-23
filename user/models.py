# -*- coding: utf-8 -*-
import datetime
from django.db import models

class User(models.Model):
    userDd = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    addTime = models.DateTimeField(default=datetime.datetime.now())
    rank = models.SmallIntegerField(default=(1,2))
    email = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    integration = models.IntegerField(default=0,blank=True)
    lastLogin = models.DateTimeField(blank=True)
    visitCount = models.IntegerField()
    mobile = models.CharField(max_length=18)
    tel = models.CharField(max_length=20)

    def __unicode__(self):
        return self.userName

    class Meta():
        db_table = "user"
        app_label = "user"



    




