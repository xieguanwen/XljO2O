# -*- coding: utf-8 -*-
import logging
from django import forms
from xiaolajiao.stores.models import StoreTemp

class StoresTempChangeForm(forms.ModelForm):
    class Meta:
        Model = StoreTemp

    def save(self, commit=True):
        storesTemp = super(StoresTempChangeForm, self).save(commit=False)
        logging.FileHandler("/tmp/xiaolajiao.log")
        logging.info("dddd")
        if commit:
            storesTemp.save()
        return storesTemp

