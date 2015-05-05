# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label=_("密码"),widget=forms.PasswordInput)