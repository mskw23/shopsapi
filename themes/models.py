# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import os

# Create your models here.
class Theme(models.Model):
    def image_upload(inatance, filename):
        return os.path.join('Volunteer', filename)
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length=100, blank=False)
    font = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=10, blank=False)
    image = models.ImageField(db_column='MyPhoto', upload_to=image_upload, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)