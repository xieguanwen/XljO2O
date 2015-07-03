# -*- coding: utf-8 -*-
import logging
from django import forms
from xiaolajiao.stores.models import StoreTemp

class StoresTempChangeForm(forms.ModelForm):
    class Meta:
        Model = StoreTemp

    def save(self, commit=True):
        storesTemp = super(StoresTempChangeForm, self).save(commit=False)
        logging.info(storesTemp,filename="/tmp/xiaoljiao.log")
        if commit:
            storesTemp.save()
        return storesTemp

