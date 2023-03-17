# Generated by Django 4.1.7 on 2023-03-16 15:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dummy_csv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scheme',
            old_name='n1',
            new_name='name_1',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n2',
            new_name='name_10',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n3',
            new_name='name_2',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n4',
            new_name='name_3',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n5',
            new_name='name_4',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n6',
            new_name='name_5',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n7',
            new_name='name_6',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n8',
            new_name='name_7',
        ),
        migrations.RenameField(
            model_name='scheme',
            old_name='n9',
            new_name='name_8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c1',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c2',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c3',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c4',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c5',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c6',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c7',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='c9',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o1',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o2',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o3',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o4',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o5',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o6',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o7',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o8',
        ),
        migrations.RemoveField(
            model_name='scheme',
            name='o9',
        ),
        migrations.AddField(
            model_name='scheme',
            name='name_9',
            field=models.CharField(blank=True, default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_10',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_6',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_7',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_8',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='order_9',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_1',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_10',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_2',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_3',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_4',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_5',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_6',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_7',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_8',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
        migrations.AddField(
            model_name='scheme',
            name='type_9',
            field=models.CharField(choices=[('1', 'Choose from...'), ('2', 'Full name'), ('3', 'Job'), ('4', 'Email'), ('5', 'Domain Name'), ('6', 'Phone number'), ('7', 'Company name'), ('8', 'Text'), ('9', 'Integer'), ('10', 'Address'), ('11', 'Date')], default='Choose from...', max_length=30),
        ),
    ]