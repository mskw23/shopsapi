# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from shops.models import Shop
from .serializers import ShopListSerializer, ShopDetailSerializer
# Create your views here.

class ShopListAPIView(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer

class ShopDetailAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    lookup_field = 'slug'