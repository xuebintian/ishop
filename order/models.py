# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cart(models.Model):   # 购物车
    user_id = models.IntegerField(null=False, default=0)
    goods_id = models.IntegerField(null=False, default=0)
    guige_list = models.CharField(null=False, max_length=128, default='')
    count = models.IntegerField(null=False, default=0)


class Order(models.Model):  # 订单
    user_id = models.IntegerField(null=False, default=0)
    address_id = models.IntegerField(null=False, default=0)
    cart_list = models.TextField(null=False, default='')
    total_price = models.IntegerField(null=False, default=0)
