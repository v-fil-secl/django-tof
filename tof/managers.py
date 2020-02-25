# -*- coding: utf-8 -*-
# @Author: MaxST
# @Date:   2019-11-17 15:02:55
# @Last Modified by:   MaxST
# @Last Modified time: 2019-11-19 16:40:49
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import get_language

from .decorators import tof_filter, tof_prefetch


class DecoratedMixIn:
    @tof_filter  # noqa
    def filter(self, *args, **kwargs):  # noqa
        return super().filter(*args, **kwargs)

    @tof_filter  # noqa
    def exclude(self, *args, **kwargs):
        return super().exclude(*args, **kwargs)

    @tof_filter  # noqa
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    @tof_filter  # noqa
    def order_by(self, *field_names):
        """Return annotate for  """
        from tof.models import Translation

        params = []
        for param in field_names:
            field_name = param
            desc = ''

            if field_name.startswith('-'):
                desc = '-'
                field_name = param[1:]

            self = self.annotate(**{f'_{field_name}': Translation.objects.filter(
                lang__iso=get_language(), field__name=field_name, object_id=models.OuterRef('pk'),
                content_type=ContentType.objects.get(model=self.model._meta.model_name,
                                                     app_label=self.model._meta.app_label)
            ).values_list('value', flat=True)})

            # not finished, breaks down ordering by fields without any translation
            params.append(f'{desc}_{field_name}')
        return super().order_by(*params)


class TranslationsQuerySet(DecoratedMixIn, models.QuerySet):
    pass


class TranslationManager(DecoratedMixIn, models.Manager):
    default_name = 'trans_objects'
    _queryset_class = TranslationsQuerySet

    def __init__(self, name=None):
        self.default_name = name or self.default_name
        super().__init__()

    @tof_prefetch()
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs)
