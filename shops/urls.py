from django.conf.urls import url
from django.contrib import admin

from views import (
    ShopListAPIView,
    ShopDetailAPIView,
    ShopUpdateAPIView,
    ShopDestroyAPIView,
    ShopCreateAPIView
    )

urlpatterns = [
    url(r'^$', ShopListAPIView.as_view(), name='list'),
    url(r'^create/$', ShopCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ShopDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ShopUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ShopDestroyAPIView.as_view(), name='destroy'),
]