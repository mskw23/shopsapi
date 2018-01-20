# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

def upload_location(instance, filename):
    PostModel = instance.__class__
    new_id = 0
    if PostModel.objects.order_by("id").last() != None:
        new_id = PostModel.objects.order_by("id").last().id + 1
    return "product/%s/%s" %(new_id, filename)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100, blank=False)
    shop = models.ForeignKey('shops.Shop', default=1, related_name='product_shop')
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True)
    price = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)