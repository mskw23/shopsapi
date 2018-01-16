# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

from .permissions import isOwnerOrReadOnly
from .pagination import ShopLimitOffsetPagination, ShopPageNumberPagination

from shops.models import Shop
from .serializers import ShopListSerializer, ShopDetailSerializer, ShopCreateUpdateSerializer
# Create your views here.

class ShopListAPIView(ListAPIView):
    serializer_class = ShopListSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']

    pagination_class = ShopPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Shop.objects.all()  # filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)
            ).distinct()
        return queryset_list

class ShopDetailAPIView(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]

class ShopUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class ShopDestroyAPIView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]

class ShopCreateAPIView(CreateAPIView):
    queryset = Shop.objects.all()

    serializer_class = ShopCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
