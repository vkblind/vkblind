# coding: utf-8

from django import forms

from .models import UserSettings


class UserSettingsForm(forms.ModelForm):
    """
    User settings form
    """
    class Meta:
        model = UserSettings
        fields = ['font_size', 'color_scheme']
