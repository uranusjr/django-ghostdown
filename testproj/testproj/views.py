#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import TestForm


def index(request):
    form = TestForm()
    return render(request, 'index.html', {'form': form})
