from django.conf.urls import url
from django.contrib import admin

from views import (
    CommentCreateAPIView,
    CommentDestroyAPIView,
    CommentListAPIView,
    CommentUpdateAPIView
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', CommentDestroyAPIView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/edit/$', CommentUpdateAPIView.as_view(), name='update'),

]