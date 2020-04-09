# -*- coding:utf-8 -*-
import logging

from django.db.utils import OperationalError

from account.models import User

logger = logging.getLogger('django')


def user_to_dict(item):
    return {
        'id': item.id,
        'username': item.username,
        'email': item.email,
        'fullname': item.fullname,
        'nickname': item.nickname,
        'gender': item.gender,
        'is_superuser': item.is_superuser
    }


# user
def get_user_list():
    try:
        user_list = []
        entry = User.objects.all()
        for e in entry:
            user_list.append(user_to_dict(e))
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e
    return user_list
