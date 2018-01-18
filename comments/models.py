# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
# Create your models here.
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs

class Comment(models.Model):
    title = models.CharField(max_length=20, blank=False)
    message = models.CharField(max_length=100, blank=False)
    shop = models.ForeignKey('shops.Shop', default=1, related_name='comment_shop')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)