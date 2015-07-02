# -*- coding: utf-8 -*-
from django import forms
from xiaolajiao.stores.models import StoreTemp

class StoresTempChangeForm(forms.ModelForm):
    class Meta:
        Model = StoreTemp

    def save(self, commit=True):
        storesTemp = super(StoresTempChangeForm, self).save(commit=False)
        if commit:
            print storesTemp.logType
            storesTemp.save()
        return storesTemp

