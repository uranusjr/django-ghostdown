#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from ghostdown.models import GhostdownField


class Post(models.Model):
    content = GhostdownField()
