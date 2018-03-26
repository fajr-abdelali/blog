# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-24 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180321_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank='True', default='default.jpg', upload_to='D:\\projects\\mn_project\\django_cms_projects'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 16, 41, 32, 268196, tzinfo=utc)),
        ),
    ]