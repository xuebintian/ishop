# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    pid = models.IntegerField(null=False, default=0)    # 父类别id
    label = models.CharField(null=False, max_length=128, default='')
    logo = models.CharField(null=False, max_length=128, default='')
    is_new = models.BooleanField(null=False, default=False)     # 分类页面可以显示new标签
    is_hot = models.BooleanField(null=False, default=False)     # 分类页面可以显示hot标签


class Goods(models.Model):
    cate_id = models.IntegerField(null=False, default=0)
    name = models.CharField(null=False, max_length=128, default='')
    main_img = models.CharField(null=False, max_length=1024, default='')
    short_desc = models.CharField(null=False, max_length=1024, default='')
    img_list = models.TextField(null=False, default='')
    detail = models.TextField(null=True, default='')

    count = models.IntegerField(null=False, default=0)  # 多种规格下的最大库存
    min_price = models.IntegerField(null=False, default=0)  # 多种规格下的最低价
    max_price = models.IntegerField(null=False, default=0)  # 多种规格下的最高价

    is_new = models.BooleanField(null=False, default=False)     # 新品，影响排序和主页显示
    is_hot = models.BooleanField(null=False, default=False)     # 手动推荐，影响排序和主页显示

    sold_count = models.IntegerField(null=False, default=0)     # 所有规格下销售量，也可以作为排序


class Guige(models.Model):  # 规格
    goods_id = models.IntegerField(null=False, default=0)
    label = models.CharField(null=False, max_length=128, default='')
    value = models.CharField(null=False, max_length=128, default='')


class Kucun(models.Model):  # 规格组合下的唯一价格
    goods_id = models.IntegerField(null=False, default=0)
    guige_list = models.CharField(null=False, max_length=128, default='')
    count = models.IntegerField(null=False, default=0)
    price = models.IntegerField(null=False, default=0)
