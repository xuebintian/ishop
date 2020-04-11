# -*- coding:utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField('nickname', max_length=100, default='', null=True)
    fullname = models.CharField('fullname', max_length=100, default='', null=False)

    wxid = models.CharField('wechat id', max_length=100, default='', null=False)

    GENDER_CHOICE = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField('gender', max_length=2, choices=GENDER_CHOICE, default='M')

    created_at = models.IntegerField('created_time', default=0)
    updated_at = models.IntegerField('updated_time', default=0)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __unicode__(self):
        return '%s-%s' % (self.fullname, self.username)


class VIP(models.Model):
    user_id = models.IntegerField(null=False, default=0)
    level = models.IntegerField(null=False, default=0)


class Address(models.Model):    # 用于下单时填写的相关信息
    user_id = models.IntegerField(null=False, default=0)
    shigongdanwei = models.CharField(null=True, max_length=128, default='')
    project_name = models.CharField(null=True, max_length=128, default='')
    project_address = models.CharField(null=True, max_length=2048, default='')
    project_contact = models.CharField(null=True, max_length=128, default='')
    shouhuoren = models.CharField(null=True, max_length=128, default='')
    shouhuoren_phone = models.CharField(null=True, max_length=128, default='')