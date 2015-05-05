# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from xiaolajiao.user.models import User

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label=_("密码"),widget=forms.PasswordInput)


    class Meta:
        Model = User
