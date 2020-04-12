# -*- coding: utf-8 -*-
import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from account import models_api

logger = logging.getLogger('django')


@login_required
def index(request):
    template = u'index.html'
    contexts = {u'title': u'ishop'}
    return render(request, template, contexts)


@login_required
def api(request):
    success = False
    message = ''
    if request.method == 'GET':
        try:
            user = request.user
            success = True
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message, 'data': None}
    # python的json.dumps方法默认会输出成这种格式"\u2535a\u35a2\u89bd"，要输出中文需要指定ensure_ascii参数为False
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def create_address(request):
    success = False
    message = ''
    pk = None
    if request.method == 'POST':
        try:
            user = request.user
            post_data = request.POST
            pk = models_api.create_address(user, post_data)
            success = True
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be POST!'

    data = {'success': success, 'message': message, 'pk': pk}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def update_address(request):
    success = False
    message = ''
    if request.method == 'POST':
        try:
            user = request.user
            post_data = request.POST
            success = models_api.update_address(user, post_data)
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')


@login_required
def delete_address(request):
    success = False
    message = ''
    if request.method == 'DELETE':
        try:
            user = request.user
            post_data = request.POST
            success = models_api.delete_address(user, post_data['id'])
        except Exception as e:
            logger.error(e)
            message = e
    else:
        message = 'request method must be GET!'

    data = {'success': success, 'message': message}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json')