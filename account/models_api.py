# -*- coding:utf-8 -*-
import logging

from django.db.utils import OperationalError

from account.models import User, Address

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


# address
def create_address(user, data):
    try:
        if hasattr(data, 'id'):
            raise Exception('地址已存在，创建失败')
        entry = Address.objects.create(
            user_id=user.id,
            shigongdanwei=data['shigongdanwei'],
            project_name=data['project_name'],
            project_address=data['project_address'],
            project_contact=data['project_contact'],
            shouhuoren=data['shouhuoren'],
            shouhuoren_phone=data['shouhuoren_phone'],
        )
        return entry.id
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e


def update_address(user, data):
    try:
        if not hasattr(data, 'id'):
            raise Exception('地址不存在，创建失败')
        entry = Address.objects.get(pk=data['id'])
        if user.id != entry.user_id:
            raise Exception('地址不存在，创建失败')
        entry.shigongdanwei = data['shigongdanwei']
        entry.project_name = data['project_name']
        entry.project_address = data['project_address']
        entry.project_contact = data['project_contact']
        entry.shouhuoren = data['shouhuoren']
        entry.shouhuoren_phone = data['shouhuoren_phone']
        entry.save()
        return True
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e


def delete_address(user, data):
    try:
        if not hasattr(data, 'id'):
            raise Exception('地址不存在，创建失败')
        entry = Address.objects.get(pk=data['id'])
        if user.id != entry.user_id:
            raise Exception('地址不存在，创建失败')
        entry.delete()
        return True
    except OperationalError as e:
        e.message = 'ErrorCode[%d]: %s' % e.args
        raise e
    except Exception as e:
        logger.error(e)
        raise e
