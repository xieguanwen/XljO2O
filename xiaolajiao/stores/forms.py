# -*- coding: utf-8 -*-
import logging
from django import forms
from xiaolajiao.stores.models import StoreTemp

class StoresTempChangeForm(forms.ModelForm):
    class Meta:
        Model = StoreTemp

    def save(self, commit=True):
        storesTemp = super(StoresTempChangeForm, self).save(commit=False)
        myLog = logging.getLogger("myLog")
        myLog.setLevel(logging.INFO)
        myLog.addHandler(logging.FileHandler("/tmp/xiaolajiao.log"))
        if commit:
            myLog.info(storesTemp.logType)
            myLog.info(storesTemp)
            myLog.info("ddd")
            storesTemp.save()
        return storesTemp

