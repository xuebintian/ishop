# -*- coding:utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    nickname = models.CharField(u'nickname', max_length=100, default='', null=True)
    fullname = models.CharField(u'fullname', max_length=100, default='', null=False)

    GENDER_CHOICE = ((u'M', u'Male'), (u'F', u'Female'),)
    gender = models.CharField(u'gender', max_length=2, choices=GENDER_CHOICE, default=u'M')

    created_at = models.IntegerField(u'created_time', default=0)
    updated_at = models.IntegerField(u'updated_time', default=0)

    class Meta(AbstractUser.Meta):
        swappable = u'AUTH_USER_MODEL'

    def __unicode__(self):
        return u'%s-%s' % (self.fullname, self.username)
