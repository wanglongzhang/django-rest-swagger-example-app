#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from snippets import views

#from xadmin.plugins import xversion
import xadmin

#version模块自动注册需要版本控制的 Model
#xversion.register_models()

xadmin.autodiscover()

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    url('^swagger/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'xadmin/', include(xadmin.site.urls)),
]
