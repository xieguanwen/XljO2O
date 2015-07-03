# -*- coding: utf-8 -*-
import logging
import sys
from django import forms
from xiaolajiao.stores.models import StoreTemp
from xiaolajiao.stores.models import Store

class StoresTempChangeForm(forms.ModelForm):
    class Meta:
        Model = StoreTemp

    def save(self, commit=True):
        storesTemp = super(StoresTempChangeForm, self).save(commit=False)
        # logging.basicConfig(filename = "/tmp/xiaolajiao.log", level = logging.INFO)
        # logging.info(storesTemp.logType)
        # logging.info(storesTemp.storeId)
        # Store.objects;
        if(storesTemp.storeId is None):
            store = Store.__init__()
        else:
            pass
        if commit:
            storesTemp.save()
        return storesTemp

