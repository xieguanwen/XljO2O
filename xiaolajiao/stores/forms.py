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
        logging.basicConfig(filename = "/tmp/xiaolajiao.log", level = logging.INFO)
        # logging.info(storesTemp.logType)
        # logging.info(storesTemp.storeId)
        # store.objects;
        if(storesTemp.storeId is None and storesTemp.logType == 0):
            store = Store()
            store.agentsId = storesTemp.agentsId
            store.userId = storesTemp.userId
            store.storeName = storesTemp.storeName
            store.province = storesTemp.province
            store.city = storesTemp.city
            store.region = storesTemp.region
            store.street = storesTemp.street
            store.address = storesTemp.address
            store.tel = storesTemp.tel
            store.contact = storesTemp.contact
            store.introduce = storesTemp.introduce
            store.license = storesTemp.license
            store.certificate = storesTemp.certificate
            store.storePicture = storesTemp.storePicture
            store.mainPicture = storesTemp.mainPicture
            store.addTime = storesTemp.addTime
            store.status = storesTemp.status
            store.longitude = storesTemp.longitude
            store.latitude = storesTemp.latitude
            store.serviceTime = storesTemp.serviceTime
            store.getThere = storesTemp.getThere
            store.logType = storesTemp.logType
            store.isOfficial = storesTemp.isOfficial
            store.save(force_insert=True)
            logging.info(store.pk)
            storesTemp.storeId = store.pk
        else:
            pass # @todo 还没有个要求
            # store = Store.objects.get(storeId = storesTemp.storeId)
            # logging.info(store)
        if commit:
            storesTemp.save()
        return storesTemp

