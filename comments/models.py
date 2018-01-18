# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=20, blank=False)
    message = models.CharField(max_length=100, blank=False)
    shop = models.ForeignKey('shops.Shop', default=1, related_name='comment_shop')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)