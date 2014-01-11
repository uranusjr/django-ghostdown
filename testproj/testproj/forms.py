#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from ghostdown.forms.widgets import GhostdownInput


class TestForm(forms.Form):
    content = forms.CharField(widget=GhostdownInput)
