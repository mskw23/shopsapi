# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from shops.models import Shop
from .serializers import ShopSerializer
# Create your views here.

class ShopListAPIView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer