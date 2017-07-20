# coding=utf-8

from django.conf.urls import url

from .views import TestView

urlpatterns = [

    url(r'^verify/?$', TestView.email_verify),
]
