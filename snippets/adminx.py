#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from .models import Snippet
import xadmin
from tutorial.util import get_field_name_list_from_model_class


# 开启后台主题样式选择
class BaseSetting(object):
    enable_themes = True
    user_bootswatch = True


# 后台全局设置
class GlobalSettings(object):
    # 后台标签
    site_title = 'ldev portal'
    # 后台页脚
    site_footer = 'ldev.com'


xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)

class SnippetAdmin(object):


    # 列表显示
    list_display = get_field_name_list_from_model_class(Snippet)
    # (
    #     'created',
    #     'title',
    #     'code',
    #     'linenos',
    #     'language',
    #     'style',
    #     'owner',
    #     'highlighted'
    # )

    # 搜索范围
    search_fields = (
        'title',
        'code',
        'language',
        'style',
        'owner',
        'highlighted'
    )
    # 列表过滤
    list_filter = (
        'created',
        'title',
        'code',
        'linenos',
        'language',
        'style',
        'owner',
        'highlighted'
    )
    # 默认排序,'-':倒序,从大到小
    ordering = ['-created']
    # 只读
    readonly_fields = ['created']
    # 刷新秒数
    refresh_times = [3, 5]
    # 直接编辑
    list_editable = ['title', 'language', 'style']

    # def queryset(self):
    #     '''
    #     过滤，将被封杀的作者过滤掉
    #     :return:
    #     '''
    #     qs = super(SnippetAdmin, self).queryset()
    #     #qs = qs.filter(is_block=False)
    #     return qs



xadmin.site.register(Snippet, SnippetAdmin)