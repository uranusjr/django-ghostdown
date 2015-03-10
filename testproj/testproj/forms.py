#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from ghostdown.forms.widgets import GhostdownInput


class BasicForm(forms.Form):
    content = forms.CharField(required=False, widget=GhostdownInput)


class PreviewForm(forms.Form):
    content = forms.CharField(
        required=False,
        widget=GhostdownInput(live_preview=True)
    )
