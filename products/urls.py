from django.conf.urls import url

from views import (
    ProductCreateAPIView,
    ProductDestroyAPIView,
    ProductListAPIView,
    ProductUpdateAPIView
    )

urlpatterns = [
    url(r'^$', ProductListAPIView.as_view(), name='list'),
    url(r'^create/$', ProductCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/delete/$', ProductDestroyAPIView.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)/edit/$', ProductUpdateAPIView.as_view(), name='update'),

]