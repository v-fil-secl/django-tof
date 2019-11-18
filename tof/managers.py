# -*- coding: utf-8 -*-
# @Author: MaxST
# @Date:   2019-11-17 15:02:55
# @Last Modified by:   MaxST
# @Last Modified time: 2019-11-17 15:06:37
from django.db import models

from .decorators import tof_filter, tof_prefetch


class TranslationsQuerySet(models.QuerySet):
    @tof_filter
    def filter(self, *args, **kwargs):  # noqa
        return super().filter(*args, **kwargs)

    @tof_filter  # noqa
    def exclude(self, *args, **kwargs):
        return super().exclude(*args, **kwargs)

    @tof_filter  # noqa
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class TranslationsManager(models.Manager):
    default_name = 'trans_objects'
    _queryset_class = TranslationsQuerySet

    def __init__(self, name=None):
        self.default_name = name or self.default_name
        super().__init__()

    @tof_filter  # noqa
    def filter(self, *args, **kwargs):  # noqa
        return super().filter(*args, **kwargs)

    @tof_filter  # noqa
    def exclude(self, *args, **kwargs):
        return super().exclude(*args, **kwargs)

    @tof_filter  # noqa
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @tof_prefetch
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)