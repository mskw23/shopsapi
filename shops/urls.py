from django.conf.urls import url
from django.contrib import admin

from views import (
    ShopListAPIView,
    ShopDetailAPIView
    )

urlpatterns = [
    url(r'^$', ShopListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ShopDetailAPIView.as_view(), name='detail')


]