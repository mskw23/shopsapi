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

from comments.models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer, CommentUpdateSerializer
# Create your views here.


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    pagination_class = ShopPageNumberPagination


class CommentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CommentDestroyAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, isOwnerOrReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
