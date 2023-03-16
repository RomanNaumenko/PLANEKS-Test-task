from django import forms
from django.db import models
from .models import Scheme


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ['name', 'author',
                  'type_1', 'type_2', 'type_3', 'type_4', 'type_5', 'type_6', 'type_7', 'type_8', 'type_9', 'type_10',
                  'name_1', 'name_2', 'name_3', 'name_4', 'name_5', 'name_6', 'name_7', 'name_8', 'name_9', 'name_10',
                  'order_1', 'order_2', 'order_3', 'order_4', 'order_5', 'order_6', 'order_7', 'order_8', 'order_9', 'order_10',
                  'rows']