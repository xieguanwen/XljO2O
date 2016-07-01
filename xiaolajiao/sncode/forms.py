# -*- coding: utf-8 -*-
from django import forms
from xiaolajiao.sncode.models import SnCodeAgents

class SnCodeAgentsChangeForm(forms.ModelForm):
    # field modify
    class Meta:
        Model = SnCodeAgents

    def save(self, commit=True):
        snCodeAgents = super(SnCodeAgentsChangeForm, self).save(commit=False)
        print(type(snCodeAgents.storeId))
        print(type(snCodeAgents))
        if(snCodeAgents.storeId is None):
            self.cleaned_data["storeId"]
            snCodeAgents.cleaned_data('storeId')
            snCodeAgents.delete('storeId')

        if(commit):
            snCodeAgents.save(update_fields=None)
        return snCodeAgents

