# -*- coding: utf-8 -*-
import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from goods import models_api

logger = logging.getLogger('django')


# @login_required
def root_category(request):
    success = False
    message = ''
    root_cate = None
    if request.method == 'GET':
        try:
            root_cate = models_api.root_category()
            success = True
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message, 'data': root_cate}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


# @login_required
def sub_category(request):
    success = False
    message = ''
    sub_cate = None
    if request.method == 'GET':
        try:
            cate_id = request.GET.get('cate_id', None)
            sub_cate = models_api.sub_category(cate_id)
            success = True
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message, 'data': sub_cate, 'cate_id': cate_id}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')
