#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import FormView, TemplateView
from .forms import BasicForm, PreviewForm


class IndexView(TemplateView):
    template_name = 'index.html'


class BasicFormView(FormView):
    form_class = BasicForm
    template_name = 'form.html'


class PreviewFormView(FormView):
    form_class = PreviewForm
    template_name = 'form.html'


index = IndexView.as_view()
basic = BasicFormView.as_view()
preview = PreviewFormView.as_view()
