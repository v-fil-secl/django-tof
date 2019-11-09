# -*- coding: utf-8 -*-
# @Author: MaxST
# @Date:   2019-10-28 20:30:42
# @Last Modified by:   MaxST
# @Last Modified time: 2019-11-09 13:42:56
from django.contrib import admin

from .models import Wine


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'active', 'sort')
