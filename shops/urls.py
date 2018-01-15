from django.conf.urls import url
from django.contrib import admin

from views import (
    ShopListAPIView
    )

urlpatterns = [
    url(r'^$', ShopListAPIView.as_view(), name='list')
]