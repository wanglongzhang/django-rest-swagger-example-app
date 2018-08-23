#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def get_field_name_list_from_model_class(model_clazz, exclude_auto_created=True):
    opts = model_clazz._meta
    return [each.verbose_name for each in sorted(opts.fields + opts.many_to_many) if each.auto_created != exclude_auto_created]