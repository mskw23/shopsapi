# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from .utils import get_read_time

# Create your models here.
class Shop(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=20, blank=False)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100, blank=False)
    theme = models.ForeignKey('themes.Theme', default=1, related_name='theme')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Shop.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    if instance.content:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var

pre_save.connect(pre_save_post_receiver, sender=Shop)