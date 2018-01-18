from django.conf.urls import url
from django.contrib import admin

from views import (
    CommentCreateAPIView,
    CommentListAPIView,
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),

]