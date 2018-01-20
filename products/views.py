# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db.models import Q

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,
)

from shops.permissions import isOwnerOrReadOnly
from shops.pagination import ShopLimitOffsetPagination, ShopPageNumberPagination

from products.models import Product
from .serializers import ProductSerializer, ProductCreateSerializer, ProductUpdateSerializer
# Create your views here.


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = ShopPageNumberPagination


class ProductUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()


class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
