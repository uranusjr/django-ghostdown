#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    FormView, TemplateView,
    CreateView, UpdateView, ListView,
)
from .models import Post
from .forms import BasicForm, PreviewForm


class GhostDownFormView(FormView):
    def get_success_url(self):
        if self.success_url is None:
            self.success_url = self.request.path
        return super(GhostDownFormView, self).get_success_url()


class IndexView(TemplateView):
    template_name = 'index.html'


class BasicFormView(GhostDownFormView):
    form_class = BasicForm
    template_name = 'form.html'


class PreviewFormView(GhostDownFormView):
    form_class = PreviewForm
    template_name = 'form.html'


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')


index = IndexView.as_view()
basic = BasicFormView.as_view()
preview = PreviewFormView.as_view()
post_list = PostListView.as_view()
post_create = PostCreateView.as_view()
post_update = PostUpdateView.as_view()
