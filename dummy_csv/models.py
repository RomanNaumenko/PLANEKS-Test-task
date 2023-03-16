from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings


class Scheme(models.Model):
    upload = models.FileField(upload_to='', blank=True)

    name = models.CharField(max_length=30, default="None", blank=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    types_of_data_choice = (('1', 'Choose from...'),
                            ('2', 'Full name'),
                            ('3', 'Job'),
                            ('4', 'Email'),
                            ('5', 'Domain Name'),
                            ('6', 'Phone number'),
                            ('7', 'Company name'),
                            ('8', 'Text'),
                            ('9', 'Integer'),
                            ('10', 'Address'),
                            ('11', 'Date'))

    type_1 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_2 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_3 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_4 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_5 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_6 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_7 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_8 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_9 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')
    type_10 = models.CharField(max_length=30, choices=types_of_data_choice, default='Choose from...')

    name_1 = models.CharField(max_length=30, default="None", blank=True)
    name_2 = models.CharField(max_length=30, default="None", blank=True)
    name_3 = models.CharField(max_length=30, default="None", blank=True)
    name_4 = models.CharField(max_length=30, default="None", blank=True)
    name_5 = models.CharField(max_length=30, default="None", blank=True)
    name_6 = models.CharField(max_length=30, default="None", blank=True)
    name_7 = models.CharField(max_length=30, default="None", blank=True)
    name_8 = models.CharField(max_length=30, default="None", blank=True)
    name_9 = models.CharField(max_length=30, default="None", blank=True)
    name_10 = models.CharField(max_length=30, default="None", blank=True)

    order_1 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_2 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_3 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_4 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_5 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_6 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_7 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_8 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_9 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    order_10 = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    rows = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name + ' (' + str(self.author) + ')' + ' ( ' + str(self.id) + 'id)'
