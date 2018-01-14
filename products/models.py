# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100, blank=False)
    shop = models.ForeignKey('Shop', default=1, related_name='shop')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)