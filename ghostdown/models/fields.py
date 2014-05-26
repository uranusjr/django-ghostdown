#!/usr/bin/env python
# -*- coding: utf-8

from django.utils.encoding import python_2_unicode_compatible
from django.utils.safestring import SafeData, mark_safe
from django.db.models.fields import TextField
from ghostdown.utils import get_render_func
from ghostdown.forms.widgets import GhostdownInput, GhostdownHiddenInput

__all__ = ['GhostdownField']


def get_rendered_field_name(field_name):
    return '_{field_name}_rendered'.format(field_name=field_name)


@python_2_unicode_compatible
class GhostdownData(SafeData):
    def __init__(self, instance, field_name, rendered_field_name):
        self.instance = instance
        self.field_name = field_name
        self.rendered_field_name = rendered_field_name

    @property
    def raw(self):
        return self.instance.__dict__.get(self.field_name)

    @raw.setter
    def raw(self, val):
        setattr(self.instance, self.field_name, val)

    @property
    def rendered(self):
        return getattr(self.instance, self.rendered_field_name)

    def __str__(self):
        return mark_safe(self.rendered)

    def __len__(self):
        return len(self.rendered)


class GhostdownDescriptor(object):
    def __init__(self, field):
        self.field = field
        self.rendered_field_name = get_rendered_field_name(self.field.name)

    def __get__(self, instance, owner):
        if instance is None:
            raise AttributeError('Can only be accessed via an instance.')
        if instance.__dict__.get(self.field.name) is None:
            return None
        return GhostdownData(
            instance, self.field.name, self.rendered_field_name
        )

    def __set__(self, obj, value):
        if isinstance(value, GhostdownData):
            obj.__dict__[self.field.name] = value.raw
            setattr(obj, self.rendered_field_name, value.rendered)
        else:
            obj.__dict__[self.field.name] = value


class GhostdownField(TextField):
    def __init__(self, *args, **kwargs):
        super(GhostdownField, self).__init__(*args, **kwargs)
        self.render_func = get_render_func()

    def contribute_to_class(self, cls, name):
        if not cls._meta.abstract:
            rendered_field = TextField(editable=False, blank=True)
            cls.add_to_class(get_rendered_field_name(name), rendered_field)
        super(GhostdownField, self).contribute_to_class(cls, name)
        setattr(cls, self.name, GhostdownDescriptor(self))

    def pre_save(self, model_instance, add):
        value = super(GhostdownField, self).pre_save(model_instance, add)
        rendered = self.render_func(value.raw)
        rendered_field_name = get_rendered_field_name(self.attname)
        setattr(model_instance, rendered_field_name, rendered)
        return value.raw

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return value.raw

    def get_prep_value(self, value, connection=None, prepared=False):
        try:
            return value.raw
        except AttributeError:
            return value

    def formfield(self, **kwargs):
        defaults = {'widget': GhostdownInput(value_path='raw')}
        defaults.update(kwargs)
        field = super(GhostdownField, self).formfield(**defaults)
        field.hidden_widget = GhostdownHiddenInput
        return field
