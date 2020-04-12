# -*- coding:utf-8 -*-
import logging

from django.db.utils import OperationalError

from goods.models import Category

logger = logging.getLogger('django')


def root_category():
    try:
        entry = list(Category.objects.filter(pid=0).values('id', 'label', 'logo', 'is_new', 'is_hot'))
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e
    return entry


def sub_category(cate_id):
    try:
        dt = []
        entry = Category.objects.filter(pid=cate_id)
        for i in entry:
            dt.append({
                'id': i.id,
                'label': i.label,
                'logo': i.logo,
                'is_new': i.is_new,
                'is_hot': i.is_hot,
                'brand': list(Category.objects.filter(pid=i.id).values('id', 'label', 'logo', 'is_new', 'is_hot'))
            })
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e
    return dt
